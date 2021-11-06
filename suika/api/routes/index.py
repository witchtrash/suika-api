from fastapi import APIRouter, Depends
from suika.main import __version__
from suika.config import get_settings, Settings
from suika.schemas.info import InfoResponse

router = APIRouter()


@router.get(
    "/",
    response_model=InfoResponse,
    summary="Get API info",
    response_description="Response containing information about the API",
)
async def index(settings: Settings = Depends(get_settings)):
    """
    Get basic API information
    """
    return {
        "name": settings.APP_NAME,
        "version": __version__,
    }
