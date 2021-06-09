"""Represents executable entrypoint for `pypi` application."""
from typing import Dict

from fastapi import FastAPI
from uvicorn import run

api = FastAPI()


@api.get('/')
async def index() -> Dict[str, str]:
    """Returns a home page."""
    return {'message': 'FastAPI homepage'}


if __name__ == "__main__":
    run(api, host='0.0.0.0', port=5001)
