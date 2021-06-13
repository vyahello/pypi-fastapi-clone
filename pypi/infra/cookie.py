import hashlib
from typing import Optional


from starlette.requests import Request
from starlette.responses import Response

auth_cookie_name = 'pypi_account'


def set_auth(response: Response, user_id: int) -> None:
    hash_val = __hash_text(str(user_id))
    value = "{}:{}".format(user_id, hash_val)
    response.set_cookie(
        auth_cookie_name, value, secure=False, httponly=True, samesite='Lax'
    )


def __hash_text(text: str) -> str:
    text = f'salty__{text}__text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_user_id_from_auth_cookie(  # noqa: CFQ004
    request: Request,
) -> Optional[int]:
    if auth_cookie_name not in request.cookies:
        return None

    value = request.cookies[auth_cookie_name]
    parts = value.split(':')
    if len(parts) != 2:
        return None

    user_id = parts[0]
    hash_val = parts[1]
    hash_val_check = __hash_text(user_id)
    if hash_val != hash_val_check:
        return None
    try:
        return int(user_id)
    except ValueError:
        return 0


def logout(response: Response) -> None:
    response.delete_cookie(auth_cookie_name)
