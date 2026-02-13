from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from core.models import Muscle
from repository.exercises import EXERCISES
from repository.recovery import TRAINED_THRESHOLD, RECOVERY

last_trained: dict[Muscle, datetime] = {}


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


def record_workout(performed: list[PerformedExercise], at: datetime) -> dict[Muscle, float]:
    load = muscle_load(performed)
    for m, l in load.items():
        if l >= TRAINED_THRESHOLD.get(m, 10.0):
            last_trained[m] = at
    return load

def trainable_muscles(now: datetime) -> list[Muscle]:
    out: list[Muscle] = []
    for m in RECOVERY.keys():
        status = recovery_status(m, now)
        if status in (RecoveryStatus.OPTIMAL, RecoveryStatus.OVERDUE, RecoveryStatus.READY):
            out.append(m)
    return out

def main() -> None:
    # - 2026-02-10: push workout
    # - 2026-02-11: pull workout
    # - 2026-02-13: check what's trainable (today-ish)

    def show_status(now: datetime) -> None:
        print(f"\n=== Status @ {now.isoformat(sep=' ', timespec='minutes')} ===")
        trainable = trainable_muscles(now)
        print("Trainable muscles:", ", ".join(m.value for m in trainable))

        # Show a few common muscles explicitly (edit to taste)
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

    show_status(datetime(2026, 2, 9, 20, 0))
    # 1) Push day: 60 pushups + 30 lateral raises + 30 triceps kickbacks
    t1 = datetime(2026, 2, 10, 18, 0)
    push_day = [
        PerformedExercise("push_up", reps=60),
        PerformedExercise("dumbbell_lateral_raise", reps=30),
        PerformedExercise("dumbbell_triceps_kickback", reps=30),
    ]
    load1 = record_workout(push_day, at=t1)
    print(f"\nRecorded workout @ {t1.isoformat(sep=' ', timespec='minutes')}")
    for m, l in sorted(load1.items(), key=lambda x: x[0].value):
        print(f"  {m.value:12s}: {l:.1f}")

    show_status(datetime(2026, 2, 10, 20, 0))

    # 2) Pull day: 40 pullups + 40 barbell rows + 30 curls
    t2 = datetime(2026, 2, 11, 18, 0)
    pull_day = [
        PerformedExercise("pull_up", reps=40),
        PerformedExercise("barbell_bent_over_row", reps=40),
        PerformedExercise("barbell_curl", reps=30),
    ]
    load2 = record_workout(pull_day, at=t2)
    print(f"\nRecorded workout @ {t2.isoformat(sep=' ', timespec='minutes')}")
    for m, l in sorted(load2.items(), key=lambda x: x[0].value):
        print(f"  {m.value:12s}: {l:.1f}")

    show_status(datetime(2026, 2, 11, 20, 0))  # same evening

    # 3) Check later (today-ish)
    show_status(datetime(2026, 2, 13, 9, 0))

    # Optional: Leg day and check again
    t3 = datetime(2026, 2, 13, 18, 0)
    leg_day = [
        PerformedExercise("barbell_back_squat", reps=40),
        PerformedExercise("rdl", reps=30),
        PerformedExercise("calf_raise", reps=60),
    ]
    load3 = record_workout(leg_day, at=t3)
    print(f"\nRecorded workout @ {t3.isoformat(sep=' ', timespec='minutes')}")
    for m, l in sorted(load3.items(), key=lambda x: x[0].value):
        print(f"  {m.value:12s}: {l:.1f}")

    show_status(datetime(2026, 2, 14, 9, 0))


if __name__ == "__main__":
    main()
