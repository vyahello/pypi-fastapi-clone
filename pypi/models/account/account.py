from starlette.requests import Request

from pypi.database.user import User
from pypi.models.base import ViewModelBase


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.user = User('Mike', 'mike@gmail.com', 'password')
