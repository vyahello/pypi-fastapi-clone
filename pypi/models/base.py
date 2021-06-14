from typing import Any, Dict, Optional

from starlette.requests import Request

from pypi.infra import cookie


class ViewModelBase:
    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = cookie.get_user_id_from_auth_cookie(
            self.request
        )
        self.is_logged_in: bool = self.user_id is not None

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__
