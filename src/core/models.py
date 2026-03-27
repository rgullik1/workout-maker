from enum import Enum
from dataclasses import dataclass
from typing import Mapping


class Muscle(str, Enum):
    CHEST = "chest"
    FRONT_DELTS = "front_delts"
    SIDE_DELTS = "side_delts"
    REAR_DELTS = "rear_delts"
    TRICEPS = "triceps"
    BICEPS = "biceps"
    FOREARMS = "forearms"
    LATS = "lats"
    UPPER_BACK = "upper_back"
    TRAPS = "traps"
    LOWER_BACK = "lower_back"
    ABS = "abs"
    OBLIQUES = "obliques"
    QUADS = "quads"
    HAMSTRINGS = "hamstrings"
    GLUTES = "glutes"
    CALVES = "calves"
    HIP_FLEXORS = "hip_flexors"
    ADDUCTORS = "adductors"
    ABDUCTORS = "abductors"
    NECK = "neck"


@dataclass(frozen=True)
class Exercise:
    id: str
    name: str
    muscles: Mapping[Muscle, float]


@dataclass(frozen=True)
class MusclePreference:
    weight: float  # 1.0 = neutral, >1 prefer more, <1 prefer less
