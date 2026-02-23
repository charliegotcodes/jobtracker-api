import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

# local default = disable; production can set require
DB_SSLMODE = os.getenv("DB_SSLMODE", "disable")

connect_args = {}
if DB_SSLMODE == "require":
    connect_args = {"sslmode": "require"}

engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)