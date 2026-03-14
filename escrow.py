wallet_balance = 100

def release_payment():
    global wallet_balance

    payment = wallet_balance
    wallet_balance = 0

    return {
        "status": "Payment Released",
        "amount": payment
    }