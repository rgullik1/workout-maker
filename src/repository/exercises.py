from core.models import Muscle, Exercise

EXERCISES: dict[str, Exercise] = {
    # ---------------- PUSH ----------------
    "push_up": Exercise(
        id="push_up",
        name="Push-up",
        muscles={
            Muscle.CHEST: 1.0,
            Muscle.TRICEPS: 0.6,
            Muscle.FRONT_DELTS: 0.4,
            Muscle.ABS: 0.2,
        },
    ),
    "barbell_overhead_press": Exercise(
        id="barbell_overhead_press",
        name="Barbell Overhead Press",
        muscles={
            Muscle.FRONT_DELTS: 1.0,
            Muscle.TRICEPS: 0.7,
            Muscle.UPPER_BACK: 0.2,
        },
    ),
    "dumbbell_lateral_raise": Exercise(
        id="dumbbell_lateral_raise",
        name="Dumbbell Lateral Raise",
        muscles={
            Muscle.SIDE_DELTS: 1.0,
            Muscle.TRAPS: 0.2,
        },
    ),
    "dumbbell_front_raise": Exercise(
        id="dumbbell_front_raise",
        name="Dumbbell Front Raise",
        muscles={
            Muscle.FRONT_DELTS: 1.0,
            Muscle.UPPER_BACK: 0.2,
        },
    ),
    "dumbbell_triceps_kickback": Exercise(
        id="dumbbell_triceps_kickback",
        name="Dumbbell Triceps Kickback",
        muscles={
            Muscle.TRICEPS: 1.0,
            Muscle.REAR_DELTS: 0.2,
        },
    ),
    "overhead_triceps_extension": Exercise(
        id="overhead_triceps_extension",
        name="Dumbbell Overhead Triceps Extension",
        muscles={
            Muscle.TRICEPS: 1.0,
        },
    ),
    # ---------------- PULL ----------------
    "pull_up": Exercise(
        id="pull_up",
        name="Pull-up",
        muscles={
            Muscle.LATS: 1.0,
            Muscle.UPPER_BACK: 0.6,
            Muscle.BICEPS: 0.5,
            Muscle.FOREARMS: 0.4,
        },
    ),
    "barbell_bent_over_row": Exercise(
        id="barbell_bent_over_row",
        name="Barbell Bent-over Row",
        muscles={
            Muscle.UPPER_BACK: 1.0,
            Muscle.LATS: 0.8,
            Muscle.BICEPS: 0.5,
            Muscle.FOREARMS: 0.4,
            Muscle.LOWER_BACK: 0.3,
        },
    ),
    "one_arm_dumbbell_row": Exercise(
        id="one_arm_dumbbell_row",
        name="One-arm Dumbbell Row",
        muscles={
            Muscle.LATS: 1.0,
            Muscle.UPPER_BACK: 0.7,
            Muscle.BICEPS: 0.5,
            Muscle.FOREARMS: 0.4,
            Muscle.REAR_DELTS: 0.3,
        },
    ),
    "dumbbell_reverse_fly": Exercise(
        id="dumbbell_reverse_fly",
        name="Dumbbell Reverse Fly",
        muscles={
            Muscle.REAR_DELTS: 1.0,
            Muscle.UPPER_BACK: 0.6,
        },
    ),
    "barbell_curl": Exercise(
        id="barbell_curl",
        name="Barbell Curl",
        muscles={
            Muscle.BICEPS: 1.0,
            Muscle.FOREARMS: 0.4,
        },
    ),
    "hammer_curl": Exercise(
        id="hammer_curl",
        name="Hammer Curl",
        muscles={
            Muscle.BICEPS: 0.8,
            Muscle.FOREARMS: 0.7,
        },
    ),
    "shrugs": Exercise(
        id="shrugs",
        name="Shrugs",
        muscles={
            Muscle.TRAPS: 1,
            Muscle.FOREARMS: 0.2,
        },
    ),
    # ---------------- LEGS ----------------
    "barbell_back_squat": Exercise(
        id="barbell_back_squat",
        name="Barbell Back Squat",
        muscles={
            Muscle.QUADS: 1.0,
            Muscle.GLUTES: 0.7,
            Muscle.ADDUCTORS: 0.4,
            Muscle.LOWER_BACK: 0.3,
        },
    ),
    "goblet_squat": Exercise(
        id="goblet_squat",
        name="Goblet Squat",
        muscles={
            Muscle.QUADS: 1.0,
            Muscle.GLUTES: 0.6,
            Muscle.ADDUCTORS: 0.3,
            Muscle.ABS: 0.2,
        },
    ),
    "rdl": Exercise(
        id="rdl",
        name="Romanian Deadlift",
        muscles={
            Muscle.HAMSTRINGS: 1.0,
            Muscle.GLUTES: 0.7,
            Muscle.LOWER_BACK: 0.4,
        },
    ),
    "calf_raise": Exercise(
        id="calf_raise",
        name="Standing Calf Raise",
        muscles={
            Muscle.CALVES: 1.0,
        },
    ),
    # ---------------- CORE ----------------
    "plank": Exercise(
        id="plank",
        name="Plank",
        muscles={
            Muscle.ABS: 1.0,
            Muscle.OBLIQUES: 0.6,
            Muscle.LOWER_BACK: 0.3,
        },
    ),
    "side_plank": Exercise(
        id="side_plank",
        name="Side Plank",
        muscles={
            Muscle.OBLIQUES: 1.0,
            Muscle.ABS: 0.6,
        },
    ),
}
