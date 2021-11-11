"""Add current price field

Revision ID: b096ed4446b2
Revises: 3eebe96462bc
Create Date: 2021-11-11 23:42:27.588832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b096ed4446b2"
down_revision = "3eebe96462bc"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("product", sa.Column("current_price", sa.Integer(), nullable=True))
    op.create_index(
        op.f("ix_product_current_price"),
        "product",
        ["current_price"],
        unique=False,
    )


def downgrade():
    op.drop_index(op.f("ix_product_current_price"), table_name="product")
    op.drop_column("product", "current_price")
