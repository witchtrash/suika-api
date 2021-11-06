from faker import Faker
from suika.schemas.product import ProductRequest


def Product() -> ProductRequest:
    fake = Faker()

    return ProductRequest(
        sku=fake.bothify(text="????####"),
        name=f"{fake.prefix_nonbinary()} {fake.color_name()}",
        volume=float(fake.random_number(digits=3, fix_len=True)),
        abv=float(fake.random_number(digits=2, fix_len=True)) / 10,
        country_of_origin=fake.country(),
        available=fake.pybool(),
        container_type=fake.random_element(elements=("Bottle", "Can", "Keg")),
        style=fake.random_element(elements=("IPA", "Pilsner", "Stout", "Hefeweizen")),
        sub_style=fake.random_element(
            elements=("Double IPA", "Imperial Stout", "Wild ale")
        ),
        producer=fake.company(),
        short_description=fake.sentence(),
        season=fake.random_element(elements=("Summer", "Winter", "Easter")),
    )
