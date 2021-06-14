from pathlib import Path
from typing import Callable, Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import Session

from pypi.tables.modelbase import SqlAlchemyBase

__factory: Optional[Callable[[], Session]] = None
__async_engine: Optional[AsyncEngine] = None


def global_init(db_file: str) -> None:
    global __factory, __async_engine

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception('You must specify a db file')

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    conn_str = 'sqlite:///' + db_file.strip()
    print('Connecting to DB with {}'.format(conn_str))  # noqa: T001

    engine = sa.create_engine(
        conn_str, echo=False, connect_args={'check_same_thread': False}
    )
    __async_engine = create_async_engine(
        conn_str, echo=False, connect_args={'check_same_thread': False}
    )
    __factory = orm.sessionmaker(bind=engine)

    import pypi.tables._models  # noqa: F401

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception('You must call global_init() before using this method')

    session: Session = __factory()
    session.expire_on_commit = False
    return session


def create_async_session() -> AsyncSession:
    global __async_engine

    if not __async_engine:
        raise Exception('You must call global_init() before using this method')

    session: AsyncSession = AsyncSession(__async_engine)
    session.sync_session.expire_on_commit = False
    return session
