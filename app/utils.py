import joblib
import pandas as pd

# loading model and encoders
model = joblib.load("model/model.pkl")
encoders = joblib.load("model/encoders.pkl")

def preprocess(data):
    # Converting pydantic model to dict
    d = data.model_dump()

    # renaming keys to match training data
    formatted = {
        "Age": d["Age"],
        "Gender": d["Gender"],
        "Blood Type": d["Blood_Type"],
        "Billing Amount": d["Billing_Amount"],
        "Admission Type": d["Admission_Type"],
        "Medication": d["Medication"],
        "Test Results": d["Test_Results"]
    }

    # Encoding categorical variables
    for col in formatted:
        if col in encoders:
            formatted[col] = encoders[col].transform([formatted[col]])[0]

    return pd.DataFrame([formatted])
