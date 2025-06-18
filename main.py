# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load model
with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# FastAPI app
app = FastAPI()

# Define the input data schema
class CustomerData(BaseModel):
    InternetService_No: int
    PaymentMethod_Electronic_check: int
    MonthlyCharges: float
    Dependents_Yes: int
    PaperlessBilling_Yes: int
    TechSupport_Yes: int
    MultipleLines_Yes: int
    OnlineSecurity_Yes: int
    tenure: float
    Contract_Two_year: int
    OnlineBackup_Yes: int
    SeniorCitizen: int
    InternetService_Fiber_optic: int
    Contract_One_year: int
    StreamingTV_Yes: int
    StreamingMovies_Yes: int


@app.post("/predict")
def predict_churn(data: CustomerData):
    input_array = np.array([[value for value in data.dict().values()]])
    prediction = model.predict(input_array)[0]
    return {"Churn Prediction": int(prediction)}
@app.get("/")
def read_root():
    return {"message": "Welcome to the churn prediction API!"}
