import datetime
import sqlalchemy
import sqlalchemy.orm as orm
from pypi.database.modelbase import SqlAlchemyBase


class Release(SqlAlchemyBase):
    __tablename__ = 'releases'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )

    major_ver = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    minor_ver = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)
    build_ver = sqlalchemy.Column(sqlalchemy.BigInteger, index=True)

    created_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now, index=True
    )
    comment: str = sqlalchemy.Column(sqlalchemy.String)
    url: str = sqlalchemy.Column(sqlalchemy.String)
    size: int = sqlalchemy.Column(sqlalchemy.BigInteger)

    # Package relationship
    package_id: str = sqlalchemy.Column(
        sqlalchemy.String, sqlalchemy.ForeignKey('packages.id')
    )
    package = orm.relation('Package')

    @property
    def version_text(self) -> str:
        return '{}.{}.{}'.format(self.major_ver, self.minor_ver, self.build_ver)
