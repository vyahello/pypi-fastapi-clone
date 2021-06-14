from starlette.requests import Request

from pypi.services import package
from pypi.models.base import ViewModelBase


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request) -> None:
        super().__init__(request)

        self.package_name = package_name
        self.latest_version = '0.0.0'
        self.is_latest = True
        self.maintainers = []
        self.package = None
        self.latest_release = None

    async def load(self) -> None:
        self.package = await package.get_package_by_id(self.package_name)
        self.latest_release = await package.get_latest_release_for_package(
            self.package_name
        )

        if not self.package or not self.latest_version:
            return None

        release = self.latest_release
        self.latest_version = (
            f'{release.major_ver}.{release.minor_ver}.{release.build_ver}'
        )
