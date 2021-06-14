from starlette.requests import Request

from pypi.models.base import ViewModelBase
from pypi.services import user


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.user = None  # type: ignore

    async def load(self) -> None:
        self.user = await user.get_user_by_id(self.user_id)
