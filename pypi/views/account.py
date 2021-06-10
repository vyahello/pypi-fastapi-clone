from typing import Any, Dict

import fastapi
from starlette.requests import Request

from pypi.models.account.account import AccountViewModel
from pypi.models.account.login import LoginViewModel
from pypi.models.account.register import RegisterViewModel

app = fastapi.FastAPI()
router = fastapi.APIRouter()


@router.get('/account')
def index(request: Request) -> Dict[str, Any]:
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
def register(request: Request) -> Dict[str, Any]:
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get('/account/login')
def login(request: Request) -> Dict[str, Any]:
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get('/account/logout')
def logout(request: Request) -> Dict[str, Any]:  # noqa: U100
    return {}
