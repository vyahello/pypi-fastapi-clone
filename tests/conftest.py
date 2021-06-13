# flake8: noqa
import pytest

from tests.mock.pypi import PyPiMock


@pytest.fixture()
def pypi_mock() -> PyPiMock:
    with PyPiMock(host='0.0.0.0', port=8080) as mock:
        return mock
