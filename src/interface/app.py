from contextlib import asynccontextmanager
from fastapi import FastAPI, Body
from datetime import datetime, timezone

import core.workout_maker as wm
from fastapi.middleware.cors import CORSMiddleware



@asynccontextmanager
async def lifespan(app: FastAPI):
    wm.load_state()
    yield

app = FastAPI(
    title="workout_app",
    version="0.0.1",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate_workout")
def generate_workout():
    now = datetime.now(timezone.utc)
    workout = wm.generate_workout(now=now)
    return {
        "at": workout.at.isoformat() if hasattr(workout, 'at') else now.isoformat(),
        "items": [
            {
                "exercise_id": item.exercise_id,
                "reps": item.reps,
            }
            for item in workout.items
        ],
    }


@app.post("/record_workout")
def record_workout(payload: dict = Body(...)):
    at_dt = datetime.now(timezone.utc)
    performed = [wm.PerformedExercise(**i) for i in payload["items"]]
    wm.record_workout(performed, at=at_dt)
    return {"status": "success", "at": at_dt.isoformat()}