from fastapi import APIRouter
from app.api.transactions.create_transaction import create_transaction, CreateTransactionResponseModel
from app.api.transactions.create_transaction_item import create_transaction_item, CreateTransactionItemResponseModel
from app.api.transactions.get_transaction_detail import get_transaction_detail, GetTransactionDetailResponseModel
from app.api.transactions.get_transaction_list import get_transaction_list, GetTransactionListResponseModel
from app.api.transactions.get_transaction_item_list import get_transaction_item_list, GetTransactionItemListResponseModel
from app.api.transactions.update_transaction import update_transaction
from app.api.transactions.cancel_transaction_item import cancel_transaction_item


api_router = APIRouter(prefix='/api')

api_router.add_api_route(
    '/v1/transactions',
    create_transaction,
    methods=['POST'],
    tags=['Transaction'],
    response_model=CreateTransactionResponseModel
)

api_router.add_api_route(
    '/v1/transaction-items',
    create_transaction_item,
    methods=['POST'],
    tags=['Transaction'],
    response_model=CreateTransactionItemResponseModel
)


api_router.add_api_route(
    '/v1/transactions/{transaction_id}',
    get_transaction_detail,
    methods=['GET'],
    tags=['Transaction'],
    response_model=GetTransactionDetailResponseModel
)


api_router.add_api_route(
    '/v1/transactions',
    get_transaction_list,
    methods=['GET'],
    tags=['Transaction'],
    response_model=GetTransactionListResponseModel
)


api_router.add_api_route(
    '/v1/transaction-items',
    get_transaction_item_list,
    methods=['GET'],
    tags=['Transaction'],
    response_model=GetTransactionItemListResponseModel
)


api_router.add_api_route(
    '/v1/transactions/{transaction_id}',
    update_transaction,
    methods=['PUT'],
    tags=['Transaction'],
    status_code=204
)


api_router.add_api_route(
    '/v1/transaction-items/{transaction_item_id}',
    cancel_transaction_item,
    methods=['DELETE'],
    tags=['Transaction'],
    status_code=204
)
