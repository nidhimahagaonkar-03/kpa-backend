from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app import schemas, crud
from app.databases import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/forms/wheel-specifications", response_model=schemas.WheelSpecOut, status_code=201)
def create_wheel_specification(spec: schemas.WheelSpecCreate, db: Session = Depends(get_db)):
    created = crud.create_wheel_spec(db, spec)
    return {
        "formNumber": created.formNumber,
        "submittedBy": created.submittedBy,
        "submittedDate": created.submittedDate,
        "status": "Saved"
    }

@router.get("/api/forms/wheel-specifications", response_model=dict)
def get_filtered_specs(
    formNumber: str = Query(None),
    submittedBy: str = Query(None),
    submittedDate: str = Query(None),
    db: Session = Depends(get_db)
):
    data = crud.get_filtered_wheel_specs(db, formNumber, submittedBy, submittedDate)
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": [
            {
                "formNumber": item.formNumber,
                "submittedBy": item.submittedBy,
                "submittedDate": item.submittedDate,
                "fields": item.fields
            }
            for item in data
        ]
    }
