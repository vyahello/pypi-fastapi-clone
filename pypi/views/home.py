from typing import Any, Dict

import fastapi
import fastapi_chameleon

router = fastapi.APIRouter()


@router.get('/')
@fastapi_chameleon.template(template_file='home/index.pt')
async def index(user: str = 'unknown') -> Dict[str, Any]:
    return {
        'package_count': 274_000,
        'release_count': 2_234_847,
        'user_count': 73_874,
        'user_name': user,
        'packages': [
            {'id': 'fastapi', 'summary': 'A great web framework'},
            {'id': 'uvicorn', 'summary': 'Your favorite ASGI server'},
            {'id': 'httpx', 'summary': 'Requests for an async world'},
        ],
    }


@router.get('/about')
@fastapi_chameleon.template(template_file='home/about.pt')
async def about() -> Dict[str, str]:
    return {}
