from starlette.requests import Request

from pypi.models.base import ViewModelBase
from pypi.services import user


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.user = user.get_user_by_id(self.user_id)  # type: ignore
