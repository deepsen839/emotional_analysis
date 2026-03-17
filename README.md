
# Emotion Reflection AI System

## Overview
This project implements a machine learning system that analyzes short user reflections and contextual signals to understand emotional state, estimate emotional intensity, and recommend helpful actions.

Components:
- Machine Learning Model
- FastAPI Backend
- React Frontend (Vite)

Architecture:
User Input → React UI → FastAPI → ML Model → Decision Engine → Recommendation

## Project Structure
emotion-ai-project/

backend/
- api.py
- state_model.pkl
- intensity_model.pkl
- label_encoder.pkl
- requirements.txt

frontend/
- package.json
- vite.config.js
- src/
  - main.jsx
  - App.jsx
  - api.js

README.md
ERROR_ANALYSIS.md
EDGE_PLAN.md

## Create Virtual Environment
python -m venv venv

Activate (Linux/Mac):
source venv/bin/activate

Activate (Windows):
venv\Scripts\activate

## Install Backend Dependencies
cd backend
pip install -r requirements.txt

requirements.txt:
fastapi
uvicorn
pandas
numpy
scikit-learn
xgboost
joblib

## Run Backend
uvicorn api:app --reload

API Docs:
http://127.0.0.1:8000/docs

## Run Frontend
cd frontend
npm install
npm run dev

Frontend URL:
http://localhost:5173

## Example Input
I feel calm after sitting near the ocean today.

## Example Output
Emotion: calm
Intensity: 2
Confidence: 0.71
Action: deep_work
When: within_15_min
