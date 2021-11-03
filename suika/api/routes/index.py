from suika.main import __version__
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def index():
  return {
    'version': f'v{__version__}'
  }
