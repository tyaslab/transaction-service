from fastapi.exceptions import HTTPException
from fastapi.params import Header
import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.models.transaction_item import TransactionItem
from app.utils.db import db_engine


async def cancel_transaction_item(transaction_item_id: int, user_id: int = Header(0, alias='X-Consumer-ID')):
    if user_id == 0:
        raise HTTPException(403, detail='Anda tidak punya hak akses')

    with Session(db_engine) as session:
        transaction_item = session.query(
            TransactionItem
        ).filter(
            TransactionItem.id == transaction_item_id
        ).first()

        if not transaction_item:
            raise HTTPException(404, detail='Item transaksi tidak ditemukan')
        
        total = transaction_item.price * (transaction_item.qty * -1)

        new_transaction_item = TransactionItem(
            transaction_id=transaction_item.transaction_id,
            user_id=user_id,
            product_id=transaction_item.product_id,
            product_name=transaction_item.product_name,
            price=transaction_item.price,
            qty=transaction_item.qty * -1,
            total=total
        )

        session.add(new_transaction_item)

        session.execute(
            sa.update(
                Transaction
            ).values(
                total=Transaction.total + total
            ).where(
                Transaction.id == transaction_item.transaction_id
            )
        )

        session.commit()
