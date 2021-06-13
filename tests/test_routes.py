import requests
from tests.mock.pypi import PyPiMock


def test_pypi_index(pypi_mock: PyPiMock) -> None:
    index_response = requests.get(pypi_mock.url)
    assert index_response.ok
    assert index_response.text == 'PyPI Clone'
