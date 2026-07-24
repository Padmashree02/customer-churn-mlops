from fastapi import FastAPI
from src.deployment.schema import CustomerData
from src.utils.model_utils import load_model
import pandas as pd

app=FastAPI()

model= load_model("models/best_model.pkl")

@app.get("/")
def home():
    return{"message":"Customer Churn API Running"}

@app.post("/predict")
def predict(data:CustomerData):
    input_data=pd.DataFrame([{
        "tenure": data.tenure,
        "MonthlyCharges":data.MonthlyCharges,
        "TotalCharges":data.TotalCharges,
        "gender":data.gender,
        "Partner":data.Partner,
        "Dependents":data.Dependents,
        "PhoneService":data.PhoneService,
        "Contract":data.Contract
    }])

    prediction=model.predict(input_data)

    prediction=int(prediction[0])

    if prediction == 1:
        result="Customer is likely to churn"
    
    else:
        result="Customer is unlikely to churn"

    return {
        "prediction":prediction,
        "result":result
        }

# user sends customer data (i/p)-> FastAPI receives JSON-> schema validate (Pydantic validates i/p)-> Data converted to Dataframe-> Preprocessing pipeline-> model predicts-> Numpy o/p converted to Python int-> API returns result