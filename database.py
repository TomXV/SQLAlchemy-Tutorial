import os

from sqlalchemy import (  # pylint: disable=unused-import
    Column,
    Float,
    Integer,
    String,
    asc,
    create_engine,
    desc,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# ----------------------------------------------------------------
# Clear Console
# ----------------------------------------------------------------


def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


# ----------------------------------------------------------------
# SQLAlchemy
# ----------------------------------------------------------------

database_file = os.path.join(os.path.abspath(os.getcwd()), "database.db")

engine = create_engine("sqlite:///" + database_file, convert_unicode=True, echo=True)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


Base = declarative_base()
Base.query = db_session.query_property()


class Table(Base):
    __tablename__ = "Table"
    id = Column(Integer, primary_key=True)
    server_id = Column(Integer, unique=False, nullable=False)
    channel_id = Column(Integer, unique=False, nullable=False)

    def __init__(self, server_id=None, channel_id=None):
        self.server_id = server_id
        self.channel_id = channel_id


Base.metadata.create_all(bind=engine)

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
    row = Table(server_id=input_server_id, channel_id=input_channel_id)
    db_session.add(row)
    db_session.commit()


def read():
    db = db_session.query(Table).all()
    print("----------------------------------------------------------------")
    print("DATABASE INFOMATION")
    print("----------------------------------------------------------------")
    for row in db:
        print("|", row.id, "|", row.server_id, "|", row.channel_id, "|")
        print("----------------------------------------------------------------")


def update():
    sel_row_num = input("Row ID?: ")
    db = db_session.query(Table).filter(Table.id == sel_row_num).first()
    db.server_id = input("Server ID?: ")
    db.channel_id = input("Channel ID?: ")
    db_session.commit()


def delete():
    sel_row_num = input("Row ID?: ")
    clearConsole()
    if sel_row_num == "ALL DELETE":
        print(
            """
----------------------------------------------------------------
NOTE: DO YOU WANT TO ALL DELETE IN THE DATABASE?
----------------------------------------------------------------
Yes: 1
No: 0
----------------------------------------------------------------
"""
        )
        sel_num = input("Number?: ")
        if sel_num == "1":
            clearConsole()
            print(
                """
----------------------------------------------------------------
NOTE: IF YOU WANTED TO UNDO YOU CAN'T IT. ARE YOU SURE DELETE?
----------------------------------------------------------------
Yes: 1
No: 0
----------------------------------------------------------------
"""
            )
        note_sel_num = input("Number?: ")
        if note_sel_num == "1":
            clearConsole()
            db_session.query(Table).delete()
            db_session.commit()

    else:
        db_session.query(Table).filter(Table.id == sel_row_num).delete()
        db_session.commit()
