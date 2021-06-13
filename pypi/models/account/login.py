from starlette.requests import Request

from pypi.models.base import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.email = ''
        self.password = ''

    async def load(self) -> None:
        form = await self.request.form()
        self.email = form.get('email', '').lower().strip()
        self.password = form.get('password', '').strip()

        if not self.email or not self.email.strip():
            self.error = 'You must specify a email.'
        elif not self.password:
            self.error = 'You must specify a password.'
