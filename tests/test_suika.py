from fastapi.testclient import TestClient
from suika.config import get_settings, get_test_settings
from suika.main import app, __version__

# Override the .env with .env.testing
app.dependency_overrides[get_settings] = get_test_settings

client = TestClient(app)


def test_index():
    settings = get_test_settings()

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "name": settings.APP_NAME,
        "version": __version__,
    }
