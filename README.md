# HealthPredictAPI 
### (ML-Powered-Patient-Condition-Forecasting)

HealthPredictAPI is a FastAPI-based machine learning service that predicts a patient’s medical condition based on demographic, billing, and medical parameters.
It returns both the predicted disease and the probability score.

The API is fully containerized using Docker.

---

## 🚀 Features

- Predict disease based on patient features
- Returns prediction + probability
- Uses a trained RandomForestClassifier
- Encodes categorical variables using saved LabelEncoders
- Clean project structure with separate preprocessing and schema validation
- Automatic interactive API docs via Swagger (/docs)
- Fully Dockerized

---

## 📁 Project Structure

```
HealthPredictAPI
├── app
│   ├── main.py
│   ├── schemas.py
│   └── utils.py
├── Healthcare-dataset.csv
├── model
│   ├── model.pkl
│   └── encoders.pkl
├── model.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

## 🧠 How It Works

1. A RandomForestClassifier is trained using the healthcare dataset.
2. Encoders for all categorical columns are saved (encoders.pkl).
3. The FastAPI service:
   - Accepts JSON input
   - Validates fields using Pydantic
   - Applies saved encoders
   - Generates prediction
   - Computes probability using model.predict_proba()
   - Returns structured JSON:

```
{
  "disease": "Diabetes",
  "probability": "76.00%"
}
```

---

## 🧪 Run Locally (Without Docker)

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Start FastAPI server
```
uvicorn app.main:app --reload
```

### 3. Open API docs
Visit: http://127.0.0.1:8000/docs

---

## 🐳 Run With Docker

### 1. Build Docker Image
```
docker build -t health-predict-api .
```

### 2. Run Container
```
docker run -p 8000:8000 health-predict-api
```

### 3. Access API Docs
http://localhost:8000/docs

---

## 📦 API Endpoints

### GET /

Health check.

**Response:**
```
{ "message": "Disease Prediction API is running" }
```

### POST /predict

Predicts disease and probability.

**Request Body:**
```
{
  "Age": 80,
  "Gender": "Male",
  "Blood_Type": "AB-",
  "Billing_Amount": 24948.47,
  "Admission_Type": "Emergency",
  "Medication": "Penicillin",
  "Test_Results": "Normal"
}
```

**Response:**
```
{
  "disease": "Hypertension",
  "probability": "66.00%"
}
```

---

## 📘 Tech Stack

- FastAPI
- scikit-learn
- RandomForest Classifier
- Pydantic
- Docker
- Python 3.10+

---

## 📌 Notes

- Model files (model.pkl, encoders.pkl) must exist in the /model directory.
- Dataset is not required at runtime - model is pre-trained.
- Docker image automatically includes the model and encoders.

---
## 😄 Enjoying the Journey

Building HealthPredictAPI has been a fun and exciting journey!  
I loved exploring FastAPI, ML models, and Docker while learning how to bring them all together. 🚀
