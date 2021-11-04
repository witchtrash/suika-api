from fastapi import APIRouter, Depends
from suika.main import __version__
from suika.config import get_settings, Settings

router = APIRouter()


@router.get("/")
async def index(settings: Settings = Depends(get_settings)):
    return {
        "name": settings.APP_NAME,
        "version": __version__,
    }
