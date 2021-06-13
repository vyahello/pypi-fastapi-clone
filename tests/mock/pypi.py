import time
from http import HTTPStatus
from types import TracebackType
from typing import Optional, Type

import fastapi
import uvicorn
from threading import Thread

import requests


def _wait_for_connection_ready(
    url: str, timeout: int = 10, poll: int = 1
) -> None:
    """Waits for connection to be up and running."""
    end_time = time.time() + timeout
    while end_time > time.time():
        try:
            session = requests.Session()
            session.get(url)
            break
        except requests.ConnectionError:
            time.sleep(poll)
    else:
        raise TimeoutError(
            f'Unable to start communication with {url} after {timeout} seconds'
        )


class PyPiMock:
    def __init__(
        self,
        host: str,
        port: int,
        ssl: bool = False,
        app: fastapi.FastAPI = fastapi.FastAPI(),
    ) -> None:
        self._app = app
        self._host = host
        self._port = port
        self._ssl = ssl
        self._running = False

    @property
    def bind(self) -> str:
        """Returns a binding address of a mock server."""
        return f"{self._host}:{self._port}"

    @property
    def url(self) -> str:
        """Returns an URL address of a mock server."""
        protocol = ('http', 'https')[self._ssl]
        return f'{protocol}://{self.bind}'

    def start(self) -> None:
        if not self._running:
            self.__compose_routes()
            thread = Thread(
                target=uvicorn.run,
                kwargs={
                    'app': self._app,
                    'host': self._host,
                    'port': self._port,
                },
            )
            thread.daemon = True
            thread.start()
            _wait_for_connection_ready(self.url)
            self._running = True

    def __enter__(self) -> 'PyPiMock':
        self.start()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],  # noqa: U100
        exc_value: Optional[BaseException],  # noqa: U100
        traceback: Optional[TracebackType],  # noqa: U100
    ) -> None:
        self._running = False

    def __compose_routes(self) -> None:
        """Builds a set of routes for mock server."""

        @self._app.get('/')
        def index() -> fastapi.responses.Response:
            return fastapi.responses.Response(
                content='PyPI Clone', status_code=int(HTTPStatus.OK)
            )
