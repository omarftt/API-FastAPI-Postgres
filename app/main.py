from fastapi import FastAPI
import models.model as model
from config import engine
from routes.user_routes import router as user_router
from routes.other_routes import router as other_router
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

app.include_router(user_router,prefix="/api",tags=["user"])
app.include_router(other_router,prefix="/other",tags=["other"])
