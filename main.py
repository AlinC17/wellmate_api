from fastapi import FastAPI, APIRouter
from fastapi_pagination import add_pagination
from core.router import register_routes


app = FastAPI(
    title="WellMate",
    description="Health check penitentiary processor"
)
add_pagination(app)


api_router = APIRouter(prefix="/api")

register_routes(api_router)
app.include_router(api_router)
