from app.database import save_transaction, CSV_DATA

def process_transaction(txn):
    key = (
        txn.transaction_id,
        float(txn.amount),
        txn.merchant,
        txn.location
    )

    if key in CSV_DATA:
        risk_percent = 10   # integer only
        decision = "APPROVED"
    else:
        risk_percent = 100  # integer only
        decision = "BLOCKED"

    # store number in DB (clean)
    save_transaction(txn, risk_percent, decision)

    # return number to frontend
    return {
        "risk_score": risk_percent,
        "decision": decision
    }

