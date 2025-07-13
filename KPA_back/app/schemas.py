from pydantic import BaseModel
from datetime import date
from typing import Dict

class WheelSpecCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]

class WheelSpecOut(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    status: str

class WheelSpecFilterOut(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: Dict[str, str]