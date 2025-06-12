from fastapi import FastAPI
from database import engine,Base
from routers import student,Authenticaton
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(student.router)
app.include_router(Authenticaton.router)