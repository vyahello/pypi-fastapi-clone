"""Represents executable entrypoint for `pypi` application."""
import fastapi
import uvicorn
import fastapi_chameleon
from starlette.staticfiles import StaticFiles

from pypi import STATIC, TEMPLATES
from pypi.views import account, home, packages

app = fastapi.FastAPI()


def main() -> None:
    configure()
    uvicorn.run(app, host='0.0.0.0', port=8080)


def configure_templates() -> None:
    fastapi_chameleon.global_init(template_folder=TEMPLATES)


def configure_routes() -> None:
    app.mount('/static', StaticFiles(directory=STATIC))
    for router in account.router, home.router, packages.router:
        app.include_router(router)


def configure() -> None:
    configure_templates()
    configure_routes()


if __name__ == '__main__':
    main()
else:
    configure()
