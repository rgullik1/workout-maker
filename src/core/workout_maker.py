from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum

from core.models import Muscle
from repository.exercises import EXERCISES
from repository.recovery import TRAINED_THRESHOLD, RECOVERY
import json
from pathlib import Path

last_trained: dict[Muscle, datetime] = {}
STATE_PATH = Path("state_last_trained.json")


def load_state() -> None:
    global last_trained
    if not STATE_PATH.exists():
        return

    data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    loaded: dict[Muscle, datetime] = {}

    for k, v in data.items():
        try:
            loaded[Muscle(k)] = datetime.fromisoformat(v)
        except Exception:
            continue

    last_trained = loaded


def save_state() -> None:
    data = {m.value: dt.isoformat() for m, dt in last_trained.items()}
    STATE_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


@dataclass(frozen=True)
class PerformedExercise:
    exercise_id: str
    reps: int


@dataclass(frozen=True)
class Workout:
    at: datetime
    items: list[PerformedExercise]


class RecoveryStatus(str, Enum):
    READY = "ready"
    RECOVERING = "recovering"
    OPTIMAL = "optimal"
    OVERDUE = "overdue"


PREFERENCES: dict[Muscle, float] = {}


def recovery_status(muscle: Muscle, now: datetime) -> RecoveryStatus:
    last = last_trained.get(muscle)
    if last is None:
        return RecoveryStatus.READY

    w = RECOVERY[muscle]
    if now < last + w.min:
        return RecoveryStatus.RECOVERING
    if now <= last + w.max:
        return RecoveryStatus.OPTIMAL
    return RecoveryStatus.OVERDUE


def muscle_load(performed: list[PerformedExercise]) -> dict[Muscle, float]:
    load: dict[Muscle, float] = {}

    for item in performed:
        exercise = EXERCISES[item.exercise_id]

        for muscle, activation in exercise.muscles.items():
            load[muscle] = load.get(muscle, 0.0) + item.reps * activation

    return load


def record_workout(
    performed: list[PerformedExercise], at: datetime
) -> dict[Muscle, float]:
    load = muscle_load(performed)
    changed = False

    for muscle, load_scalar in load.items():
        if load_scalar >= TRAINED_THRESHOLD.get(muscle, 10.0):
            last_trained[muscle] = at
            changed = True

    if changed:
        save_state()

    return load


def trainable_muscles(now: datetime) -> list[Muscle]:
    out: list[Muscle] = []
    for m in RECOVERY.keys():
        status = recovery_status(m, now)
        if status in (
            RecoveryStatus.OPTIMAL,
            RecoveryStatus.OVERDUE,
            RecoveryStatus.READY,
        ):
            out.append(m)
    return out


def generate_workout(
    now: datetime,
    reps: int = 30,
    preferences: dict[Muscle, float] | None = None,
) -> Workout:
    preferences = preferences or {}
    candidates = trainable_muscles(now)

    def status_priority(m: Muscle) -> int:
        status = recovery_status(m, now)
        if status == RecoveryStatus.OVERDUE:
            return 0
        if status == RecoveryStatus.READY:
            return 1
        if status == RecoveryStatus.OPTIMAL:
            return 2
        return 3

    def candidate_score(m: Muscle) -> tuple[int, float]:
        pref = preferences.get(m, 1.0)
        return (status_priority(m), -pref)

    candidates.sort(key=candidate_score)

    performed: list[PerformedExercise] = []
    used_exercise_ids: set[str] = set()
    exercise_limit = 5

    for muscle in candidates:
        status = recovery_status(muscle, now)
        if status not in (
            RecoveryStatus.READY,
            RecoveryStatus.OPTIMAL,
            RecoveryStatus.OVERDUE,
        ):
            continue

        best_id: str | None = None
        best_score = 0.0

        for ex_id, ex in EXERCISES.items():
            if ex_id in used_exercise_ids:
                continue

            activation = ex.muscles.get(muscle, 0.0)
            if activation <= 0.0:
                continue

            pref = preferences.get(muscle, 1.0)
            score = activation * pref

            if score > best_score:
                best_score = score
                best_id = ex_id

        if best_id is None:
            continue

        used_exercise_ids.add(best_id)
        performed.append(PerformedExercise(exercise_id=best_id, reps=reps))

        if len(performed) >= exercise_limit:
            break

    return Workout(at=now, items=performed)


def main() -> None:
    def show_status(now: datetime) -> None:
        print(f"=== Status @ {now.isoformat(sep=' ', timespec='minutes')} ===")
        trainable = trainable_muscles(now)
        print("Trainable muscles:", ", ".join(m.value for m in trainable))

        for m in [
            Muscle.CHEST,
            Muscle.TRICEPS,
            Muscle.FRONT_DELTS,
            Muscle.LATS,
            Muscle.UPPER_BACK,
            Muscle.BICEPS,
            Muscle.QUADS,
            Muscle.HAMSTRINGS,
            Muscle.GLUTES,
            Muscle.ABS,
        ]:
            print(f"{m.value:12s} -> {recovery_status(m, now).value}")

    def new_day(t: datetime, i) -> None:
        print("\n=== New Day ===")
        print("======================================================= ")
        print("======================================================= ")
        print("======================================================= ")

        show_status(t)
        workout = generate_workout(t, reps=30)
        print(f"\nGenerated workout{i}:")
        for exercise in workout.items:
            print(
                f"  - {EXERCISES[exercise.exercise_id].name} ({exercise.exercise_id}): {exercise.reps} reps"
            )
        load = record_workout(workout.items, at=t)
        print(f"\nRecorded workout @ {t.isoformat(sep=' ', timespec='minutes')}")
        for muscle, load_scalar in sorted(load.items(), key=lambda x: x[0].value):
            print(f"  {muscle.value:12s}: {load_scalar:.1f}")
        show_status(t)

    now = datetime.now()
    for i in range(30):
        new_day(now, i)
        now = now + timedelta(days=1)


if __name__ == "__main__":
    main()
