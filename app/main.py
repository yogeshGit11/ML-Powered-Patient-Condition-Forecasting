from fastapi import FastAPI
from app.schemas import PredictRequest
from app.utils import model, encoders, preprocess

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Yogesh... Disease Prediction API is running"}

@app.post("/predict")
def predict_disease(request: PredictRequest):
    df = preprocess(request)
    predict = model.predict(df)[0]
    prediction_proba = model.predict_proba(df)[0]
    probability = max(prediction_proba) * 100
    disease_name = encoders['Medical Condition'].inverse_transform([predict])[0]
    return {"disease": disease_name, "probability": f"{probability:.2f}%"}
