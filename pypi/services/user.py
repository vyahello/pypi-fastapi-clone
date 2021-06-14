from typing import Optional

from pypi.database.user import User

__fake_password = 'abc'
__fake_user = 'test'


def user_count() -> int:
    return 73_448


def create_account(name: str, email: str, password: str) -> User:
    return User(name, email, password)


def login_user(email: str, password: str) -> Optional[User]:
    if password == __fake_password:
        return User(__fake_user, email, __fake_password)
    return None
