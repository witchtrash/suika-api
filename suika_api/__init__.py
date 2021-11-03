__version__ = '0.1.0'

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_app():
  return { 'version': f'suika v{__version__}' }
