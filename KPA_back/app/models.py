from sqlalchemy import Column, Integer, String, JSON, Date
from app.databases import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, nullable=False)
    submittedBy = Column(String, nullable=False)
    submittedDate = Column(Date, nullable=False)
    fields = Column(JSON, nullable=False)  # Store nested fields as JSON