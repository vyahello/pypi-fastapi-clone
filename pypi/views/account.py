import asyncio
from typing import Any, Dict

import fastapi
import fastapi_chameleon
from starlette import status
from starlette.requests import Request

from pypi.infra import cookie
from pypi.models.account.account import AccountViewModel
from pypi.models.account.login import LoginViewModel
from pypi.models.account.register import RegisterViewModel
from pypi.services import user

app = fastapi.FastAPI()
router = fastapi.APIRouter()


@router.get('/account')
@fastapi_chameleon.template()
async def index(request: Request) -> Dict[str, Any]:
    account_vm = AccountViewModel(request)
    await account_vm.load()
    return account_vm.to_dict()


@router.get('/account/register')
@fastapi_chameleon.template()
def register(request: Request) -> Dict[str, Any]:  # noqa: F811
    register_vm = RegisterViewModel(request)
    return register_vm.to_dict()


@router.post('/account/register')  # type: ignore  # noqa: F811
@fastapi_chameleon.template()
async def register(  # noqa: F811
    request: Request,
) -> fastapi.responses.RedirectResponse:
    register_vm = RegisterViewModel(request)
    await register_vm.load()

    if register_vm.error:
        return register_vm.to_dict()
    account = await user.create_account(
        register_vm.name, register_vm.email, register_vm.password
    )
    response = fastapi.responses.RedirectResponse(
        url='/account', status_code=status.HTTP_302_FOUND
    )
    cookie.set_auth(response, account.id)

    return response


@router.get('/account/login')
@fastapi_chameleon.template(template_file='account/login.pt')
def login(request: Request) -> Dict[str, Any]:
    login_vm = LoginViewModel(request)
    return login_vm.to_dict()


@router.post('/account/login')  # type: ignore  # noqa: F811
@fastapi_chameleon.template(template_file='account/login.pt')
async def login(request: Request) -> Dict[str, Any]:  # noqa: F811
    login_vm = LoginViewModel(request)
    await login_vm.load()

    if login_vm.error:
        return login_vm.to_dict()

    logged_user = await user.login_user(login_vm.email, login_vm.password)
    if not logged_user:
        await asyncio.sleep(5)
        login_vm.error = "The account does not exist or the password is wrong."
        return login_vm.to_dict()

    response = fastapi.responses.RedirectResponse(
        '/account', status_code=status.HTTP_302_FOUND
    )
    cookie.set_auth(response, logged_user.id)
    return response


@router.get('/account/logout')
def logout() -> fastapi.responses.RedirectResponse:
    response = fastapi.responses.RedirectResponse(
        url='/', status_code=status.HTTP_302_FOUND
    )
    cookie.logout(response)
    return response
