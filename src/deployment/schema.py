from pydantic import BaseModel

class CustomerData(BaseModel):
    
    #validates the data
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender: str
    Partner: str
    Dependents: str
    PhoneService: str
    Contract: str