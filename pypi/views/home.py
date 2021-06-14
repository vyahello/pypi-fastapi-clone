from typing import Any, Dict

import fastapi
import fastapi_chameleon
from starlette.requests import Request

from pypi.models.base import ViewModelBase
from pypi.models.home.index import IndexViewModel  # type: ignore

router = fastapi.APIRouter()


@router.get('/')
@fastapi_chameleon.template()
async def index(request: Request) -> Dict[str, Any]:
    index_model = IndexViewModel(request)
    await index_model.load()
    return index_model.to_dict()


@router.get('/about')
@fastapi_chameleon.template()
async def about(request: Request) -> Dict[str, Any]:
    base_vm = ViewModelBase(request)
    return base_vm.to_dict()
