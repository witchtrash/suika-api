"""Add indices

Revision ID: 3eebe96462bc
Revises: ec88dd44f084
Create Date: 2021-11-11 02:55:30.145069

"""
from alembic import op
import sqlalchemy as sa  # noqa: F401


# revision identifiers, used by Alembic.
revision = "3eebe96462bc"
down_revision = "ec88dd44f084"
branch_labels = None
depends_on = None


def upgrade():
    op.create_index(op.f("ix_price_price"), "price", ["price"], unique=False)
    op.create_index(op.f("ix_price_product_id"), "price", ["product_id"], unique=False)
    op.create_index(op.f("ix_product_abv"), "product", ["abv"], unique=False)
    op.create_index(op.f("ix_product_name"), "product", ["name"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_product_name"), table_name="product")
    op.drop_index(op.f("ix_product_abv"), table_name="product")
    op.drop_index(op.f("ix_price_product_id"), table_name="price")
    op.drop_index(op.f("ix_price_price"), table_name="price")
