import os
import pytest

os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")

from sqlmodel import SQLModel
from app.db import engine


@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)