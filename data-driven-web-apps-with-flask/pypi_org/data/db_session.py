import sqlalchemy as sa
import sqlalchemy.orm as orm

from pypi_org.data.modelbase import SqlAlchemyBase

factory = None


def global_init(db_file: str):
    global factory

    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("YOu must specify a db file.")

    conn_str = "sqlite:///" + db_file.strip()
    print(f"Connecting to DB with {conn_str}")

    engine = sa.create_engine(conn_str, echo=True)
    factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import pypi_org.data.__all_models

    SqlAlchemyBase.metadata.create_all(engine)