from suika.config import get_test_settings
from suika.main import __version__
from suika.schemas.info import InfoResponse


def test_info(app):
    settings = get_test_settings()

    response = app.get("/")
    json: InfoResponse = response.json()

    assert response.status_code == 200
    assert json["version"] == __version__
    assert json["name"] == settings.APP_NAME
