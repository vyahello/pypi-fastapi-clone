import datetime
from typing import Dict, List, Optional

from pypi.database.package import Package
from pypi.database.release import Release


def release_count() -> int:
    return 2_234_847


def package_count() -> int:
    return 274_000


def latest_packages(limit: int = 5) -> List[Dict[str, str]]:
    return [
        {'id': 'fastapi', 'summary': 'A great web framework'},
        {'id': 'uvicorn', 'summary': 'Your favorite ASGI server'},
        {'id': 'httpx', 'summary': 'Requests for an async world'},
    ][:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name,
        'This is the summary',
        'Full details here',
        'https://github.com/vyahello/pypi',
        'MIT',
        'VLADIMIR YAHELLO',
    )
    return package


def get_latest_release_for_package(
    package_name: str,  # noqa: U100
) -> Optional[Release]:
    return Release('1.2.0', datetime.datetime.now())
