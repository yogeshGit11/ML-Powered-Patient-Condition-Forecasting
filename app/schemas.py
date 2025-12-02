from pydantic import BaseModel

class PredictRequest(BaseModel):
    Age: int
    Gender: str
    Blood_Type: str
    Billing_Amount: float
    Admission_Type: str
    Medication: str
    Test_Results: str
