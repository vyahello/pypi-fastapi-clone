from typing import Dict

import fastapi

app = fastapi.FastAPI()
router = fastapi.APIRouter()


@router.get('/account')
async def account() -> Dict[str, str]:
    return {}


@router.get('/account/register')
async def register() -> Dict[str, str]:
    return {}


@router.get('/account/login')
async def login() -> Dict[str, str]:
    return {}


@router.get('/account/logout')
async def logout() -> Dict[str, str]:
    return {}
