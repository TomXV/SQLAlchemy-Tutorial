import os
from sqlalchemy import create_engine, asc, desc, Column, Integer, Float, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ----------------------------------------------------------------
# SQLAlchemy
# ----------------------------------------------------------------

database_file = os.path.join(os.path.abspath(os.getcwd()), 'database.db')

engine = create_engine('sqlite:///' + database_file, convert_unicode=True, echo=True)

db_session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = engine
    )
)


Base = declarative_base()
Base.query = db_session.query_property()

class Table(Base):
    __tablename__ = 'Table'
    id = Column(Integer, primary_key=True)
    server_id = Column(Integer, unique=False, nullable=False)
    channel_id = Column(Integer, unique=False, nullable=False)

    def __init__(self, server_id = None, channel_id = None):
        self.server_id = server_id
        self.channel_id = channel_id

        Base.metadata.create_all(bind = engine)

# ----------------------------------------------------------------
# CRUD操作 (Create, read, update, delete)
# ----------------------------------------------------------------
# db_session.query(Table).filter().all()
# db_session.query(Table).limit(20).all()
# db_session.query(Table).first()
# db_session.query(Table).order_by(asc())
# db_session.query(Table).order_by(desc())
# ----------------------------------------------------------------

def create():
    input_server_id = input("Server ID?: ")
    input_channel_id = input("Channel ID?: ")
    row = Table(server_id =input_server_id, channel_id = input_channel_id)
    db_session.add(row)
    db_session.commit()


def read():
    db = db_session.query(Table).all()
    for row in db:
        print(row.id, row.server_id, row.channel_id)


def update():
    select_id = input("Row ID?: ")
    db = db_session.query(Table).filter(Table.id == select_id).first()
    db.server_id = input("Server ID?: ")
    db.channel_id = input("Channel ID?: ")
    db_session.commit()


def delete():
    select_id = input("Row ID?: ")
    db = db_session.query(Table).filter(Table.id == select_id).delete()