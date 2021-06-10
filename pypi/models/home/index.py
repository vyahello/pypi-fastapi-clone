from typing import Any, Dict, List

from starlette.requests import Request

from pypi.services import package, user
from pypi.models.base import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.release_count: int = package.release_count()
        self.user_count: int = user.user_count()
        self.package_count: int = package.package_count()
        self.packages: List[Dict[str, Any]] = package.latest_packages(limit=5)
