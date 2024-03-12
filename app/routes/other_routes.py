from fastapi import APIRouter, BackgroundTasks
from schemas.schemas import Response
from routes.user_routes import counter
from utils.tools import counter_timer


router = APIRouter()


@router.get("/v1/contador")
async def contador():
    return Response(code=200, status="OK", message="Counter called", result=counter[0]).dict(exclude_none=True)


@router.get("/v1/contador_timer")
async def obtener_contador():
    return Response(code=200, status="OK", message="Counter timed called", result=counter_timer[0]).dict(exclude_none=True)

