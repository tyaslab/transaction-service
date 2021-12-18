import sqlalchemy as sa
from sqlalchemy.orm import Session
from fastapi import Header
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from app.api_models import BaseResponseModel
from app.models.transaction import Transaction, TransactionStatus
from app.models.product import Product
from app.models.transaction_item import TransactionItem
from app.utils.db import db_engine


class CreateTransactionItemData(BaseModel):
    transaction_id: int
    product_id: int
    price: int
    qty: int


class CreateTransactionItemResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id': 1,
                    'url': '/api/v1/transaction-items/1'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def create_transaction_item(data: CreateTransactionItemData, user_id: int = Header(0, alias='X-Consumer-ID')):
    if user_id == 0:
        raise HTTPException(403, detail='Anda tidak punya hak akses')
    
    with Session(db_engine) as session:
        # check transaction
        transaction = session.query(
            Transaction.id, Transaction.status
        ).filter(
            Transaction.id == data.transaction_id
        ).first()

        if not transaction:
            raise HTTPException(400, detail='Transaksi tidak ditemukan')
        
        if transaction.status > TransactionStatus.OUTSTANDING:
            raise HTTPException(400, detail='Transaksi sudah selesai jadi tidak bisa menambahkan item lagi')

        # check product
        product = session.query(
            Product.id, Product.name
        ).filter(
            Product.id == data.product_id
        ).filter(
            Product.is_active
        ).first()

        if not product:
            raise HTTPException(400, detail='Product tidak ditemukan')
        
        total = data.price * data.qty

        transaction_item = TransactionItem(
            user_id=user_id,
            transaction_id=data.transaction_id,
            product_id=data.product_id,
            product_name=product.name,
            price=data.price,
            qty=data.qty,
            total=total
        )

        session.add(transaction_item)

        # add total transaction
        session.execute(
            sa.update(
                Transaction
            ).values(
                total=Transaction.total + total
            ).where(
                Transaction.id == data.transaction_id
            )
        )

        session.commit()

        return CreateTransactionItemResponseModel(
            data={
                'id': transaction_item.id,
                'url': f'/api/v1/transaction-items/{transaction_item.id}'
            }
        )
