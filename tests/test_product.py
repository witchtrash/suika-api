from suika.models.product import Product as ProductModel


def test_get_products(app, db, product):
    products = [product() for _ in range(5)]

    for product in products:
        db.add(ProductModel(**product.dict()))

    db.commit()

    response = app.get("/product")
    json = response.json()
    assert response.status_code == 200
    assert len(json) == 5
