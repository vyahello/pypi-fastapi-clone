from typing import Any, List

from starlette.requests import Request

from pypi.services import package
from pypi.models.base import ViewModelBase


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request) -> None:
        super().__init__(request)

        self.package_name = package_name
        self.package = package.get_package_by_id(package_name)
        self.latest_release = package.get_latest_release_for_package(
            package_name
        )
        self.latest_version = '0.0.0'
        self.is_latest = True
        self.maintainers: List[Any] = []

        if not self.package or not self.latest_version:
            return

        release = self.latest_release
        self.latest_version = (
            f'{release.major_ver}.'  # type: ignore
            f'{release.minor_ver}.{release.build_ver}'
        )
        self.maintainers = []
