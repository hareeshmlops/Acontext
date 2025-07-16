from fastapi import FastAPI
from contextlib import asynccontextmanager
from acontext_server.api.api_v1 import router as api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_v1_router, prefix="/api/v1")
