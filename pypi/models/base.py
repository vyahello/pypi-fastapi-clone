from typing import Any, Dict, Optional

from starlette.requests import Request


class ViewModelBase:
    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = None
        self.is_logged_in: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__
