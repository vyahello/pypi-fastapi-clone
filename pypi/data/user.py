import datetime
from typing import Optional


class User:
    def __init__(self, name: str, email: str, hash_password: str) -> None:
        self.id = 1
        self.name = name
        self.email = email
        self.hash_password = hash_password
        self.created_date = None
        self.profile_image_url = ''
        self.last_login: Optional[datetime.datetime] = None
