from fastapi import APIRouter, Depends
from suika.main import __version__
from suika.config import get_settings, Settings
from suika.schemas.info import Info

router = APIRouter()


@router.get("/", response_model=Info)
async def index(settings: Settings = Depends(get_settings)):
    return {
        "name": settings.APP_NAME,
        "version": __version__,
    }
