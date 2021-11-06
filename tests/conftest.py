from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from suika.main import app as suika
from suika.config import get_settings, get_test_settings
from suika.core.db import get_db, Base


@pytest.fixture(scope="module")
def app():
    test_settings = get_test_settings()
    engine = create_engine(test_settings.SQLALCHEMY_DATABASE_URI)

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    def get_test_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Override the .env with .env.testing
    suika.dependency_overrides[get_settings] = get_test_settings
    suika.dependency_overrides[get_db] = get_test_db

    # Create all the database tables
    Base.metadata.create_all(bind=engine)

    yield TestClient(suika)

    # Teardown, runs after the test
    Base.metadata.drop_all(bind=engine)
