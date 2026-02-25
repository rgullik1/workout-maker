from contextlib import asynccontextmanager
from fastapi import FastAPI
from datetime import datetime, timezone

import core.workout_maker as wm


@asynccontextmanager
async def lifespan(app: FastAPI):
    wm.load_state()
    yield

app = FastAPI(
    title="workout_app",
    version="0.0.1",
    lifespan=lifespan,
)


@app.get("/generate_workout")
def generate_workout():
    now = datetime.now(timezone.utc)
    workout = wm.generate_workout(now=now)
    wm.record_workout(workout.items, at=now)
    return {
        "at": workout.at.isoformat(),
        "items": [
            {
                "exercise_id": item.exercise_id,
                "reps": item.reps,
            }
            for item in workout.items
        ],
    }