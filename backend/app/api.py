from fastapi import APIRouter
from app.schemas import TransactionIn
from app.services import process_transaction

router = APIRouter(prefix="/api")

@router.post("/transaction")
def check_transaction(txn: TransactionIn):
    return process_transaction(txn)
