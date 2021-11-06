def test_product(app):
    response = app.get("/product")

    assert response.status_code == 200
