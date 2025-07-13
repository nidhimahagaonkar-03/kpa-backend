from fastapi import FastAPI
from app.databases import Base, engine
from app.routers import wheel_spec

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(wheel_spec.router)