from fastapi import FastAPI
from database import Base, engine

from api.users_api.users import users_router
from api.Jobs_api.jobs import jobs_router

Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/")
app.include_router(users_router)
app.include_router(jobs_router)
