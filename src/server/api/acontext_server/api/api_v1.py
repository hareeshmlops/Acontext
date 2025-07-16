from contextlib import asynccontextmanager
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from ..schema.pydantic.response import BasicResponse

router = APIRouter()


@router.get("/ping", tags=["chore"])
async def ping() -> BasicResponse:
    return BasicResponse(data={"message": "pong"})
