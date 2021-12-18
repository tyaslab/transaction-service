import sqlalchemy as sa
from sqlalchemy.dialects.mysql import TINYINT
from app.models import Base


class Product(Base):
    __tablename__ = 'Product'

    id = sa.Column('id', sa.Integer, primary_key=True)
    barcode = sa.Column('barcode', sa.String)
    name = sa.Column('name', sa.String)
    price = sa.Column('price', sa.Integer)
    is_active = sa.Column('is_active', TINYINT)
    created_at = sa.Column('created_at', sa.DateTime)
    modified_at = sa.Column('modified_at', sa.DateTime)
