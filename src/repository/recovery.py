from dataclasses import dataclass
from datetime import timedelta

from core.models import Muscle


@dataclass(frozen=True)
class RecoveryWindow:
    min: timedelta
    max: timedelta


RECOVERY: dict[Muscle, RecoveryWindow] = {
    # Upper body push
    Muscle.CHEST: RecoveryWindow(timedelta(days=2), timedelta(days=3)),
    Muscle.FRONT_DELTS: RecoveryWindow(timedelta(days=1), timedelta(days=2)),
    Muscle.SIDE_DELTS: RecoveryWindow(timedelta(days=1), timedelta(days=2)),
    Muscle.TRICEPS: RecoveryWindow(timedelta(days=2), timedelta(days=3)),
    # Upper body pull
    Muscle.LATS: RecoveryWindow(timedelta(days=2), timedelta(days=4)),
    Muscle.UPPER_BACK: RecoveryWindow(timedelta(days=2), timedelta(days=4)),
    Muscle.REAR_DELTS: RecoveryWindow(timedelta(days=1), timedelta(days=2)),
    Muscle.BICEPS: RecoveryWindow(timedelta(days=2), timedelta(days=3)),
    Muscle.FOREARMS: RecoveryWindow(timedelta(days=1), timedelta(days=2)),
    Muscle.TRAPS: RecoveryWindow(timedelta(days=2), timedelta(days=3)),
    Muscle.NECK: RecoveryWindow(timedelta(days=1), timedelta(days=2)),
    # Core
    Muscle.ABS: RecoveryWindow(timedelta(days=1), timedelta(days=2)),
    Muscle.OBLIQUES: RecoveryWindow(timedelta(days=1), timedelta(days=2)),
    Muscle.LOWER_BACK: RecoveryWindow(timedelta(days=2), timedelta(days=4)),
    # Lower body
    Muscle.QUADS: RecoveryWindow(timedelta(days=3), timedelta(days=5)),
    Muscle.HAMSTRINGS: RecoveryWindow(timedelta(days=3), timedelta(days=4)),
    Muscle.GLUTES: RecoveryWindow(timedelta(days=3), timedelta(days=4)),
    Muscle.CALVES: RecoveryWindow(timedelta(days=2), timedelta(days=3)),
    Muscle.HIP_FLEXORS: RecoveryWindow(timedelta(days=2), timedelta(days=3)),
    Muscle.ADDUCTORS: RecoveryWindow(timedelta(days=2), timedelta(days=3)),
    Muscle.ABDUCTORS: RecoveryWindow(timedelta(days=2), timedelta(days=3)),
}

TRAINED_THRESHOLD: dict[Muscle, float] = {
    Muscle.CHEST: 10.0,
    Muscle.TRICEPS: 8.0,
    Muscle.FRONT_DELTS: 6.0,
    Muscle.SIDE_DELTS: 6.0,
    Muscle.REAR_DELTS: 6.0,
    Muscle.LATS: 10.0,
    Muscle.UPPER_BACK: 10.0,
    Muscle.BICEPS: 8.0,
    Muscle.FOREARMS: 6.0,
    Muscle.TRAPS: 8.0,
    Muscle.NECK: 5.0,
    Muscle.ABS: 8.0,
    Muscle.OBLIQUES: 6.0,
    Muscle.LOWER_BACK: 8.0,
    Muscle.QUADS: 12.0,
    Muscle.HAMSTRINGS: 10.0,
    Muscle.GLUTES: 10.0,
    Muscle.CALVES: 8.0,
    Muscle.HIP_FLEXORS: 6.0,
    Muscle.ADDUCTORS: 8.0,
    Muscle.ABDUCTORS: 8.0,
}
