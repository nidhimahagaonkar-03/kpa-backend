from sqlalchemy.orm import Session
from app import models, schemas

def create_wheel_spec(db: Session, spec: schemas.WheelSpecCreate):
    db_spec = models.WheelSpecification(**spec.dict())
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec

def get_filtered_wheel_specs(db: Session, formNumber=None, submittedBy=None, submittedDate=None):
    query = db.query(models.WheelSpecification)
    if formNumber:
        query = query.filter(models.WheelSpecification.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submittedDate == submittedDate)
    return query.all()