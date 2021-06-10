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
        self.maintainers = []

        if not self.package or not self.latest_version:
            return

        self.latest_version = self.latest_release.version  # type: ignore
        self.maintainers = self.package.maintainers
