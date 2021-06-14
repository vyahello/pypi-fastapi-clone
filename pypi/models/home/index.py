# type: ignore
from typing import Any, Dict, List

from starlette.requests import Request

from pypi.services import package, user
from pypi.models.base import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.release_count: int = 0
        self.user_count: int = 0
        self.package_count: int = 0
        self.packages: List = []

    async def load(self) -> None:
        self.release_count: int = await package.release_count()
        self.user_count: int = await user.user_count()
        self.package_count: int = await package.package_count()
        self.packages: List[Dict[str, Any]] = await package.latest_packages(
            limit=5
        )
