from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import joblib

app = FastAPI()

# allow React to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

state_model = joblib.load("state_model.pkl")
intensity_model = joblib.load("intensity_model.pkl")
le = joblib.load("label_encoder.pkl")


def decision_engine(state, intensity, stress, energy, time_of_day):

    if stress >= 4:
        return "box_breathing","now"

    if state == "restless":
        return "movement","within_15_min"

    if state == "calm" and energy >= 4:
        return "deep_work","within_15_min"

    if energy <= 2:
        return "rest","later_today"

    if time_of_day == "night":
        return "journaling","tonight"

    return "light_planning","later_today"


def supportive_message(state, action):

    if action == "box_breathing":
        return "You seem tense. Try a short breathing exercise."

    if action == "deep_work":
        return "Your energy looks good. This is a great time for focused work."

    if action == "rest":
        return "Your energy seems low. Consider resting."

    return "Take a moment to slow down and reflect."


@app.post("/predict")
def predict(data: dict):

    sample = pd.DataFrame({
        "journal_text":[data["journal_text"]],
        "ambience_type":[data["ambience_type"]],
        "duration_min":[data["duration_min"]],
        "sleep_hours":[data["sleep_hours"]],
        "energy_level":[data["energy_level"]],
        "stress_level":[data["stress_level"]],
        "time_of_day":[data["time_of_day"]],
        "previous_day_mood":[data["previous_day_mood"]],
        "face_emotion_hint":[data["face_emotion_hint"]],
        "reflection_quality":[data["reflection_quality"]]
    })

    probs = state_model.predict_proba(sample)
    pred = np.argmax(probs, axis=1)

    emotion = le.inverse_transform(pred)[0]
    confidence = float(np.max(probs))

    intensity = float(intensity_model.predict(sample)[0])

    action, when = decision_engine(
        emotion,
        intensity,
        data["stress_level"],
        data["energy_level"],
        data["time_of_day"]
    )

    message = supportive_message(emotion, action)

    return {
        "predicted_state": emotion,
        "predicted_intensity": intensity,
        "confidence": confidence,
        "what_to_do": action,
        "when_to_do": when,
        "supportive_message": message
    }