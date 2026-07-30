class InsufficientFundsError(Exception): # Exception class ko inherit kr liya haii
    pass

def withdraw_money(balance:int, amount:int):
    if balance < amount:
        raise InsufficientFundsError("Not enough balance")
    print(f"Remaining balance = {balance-amount}")

# withdraw_money(1000, 5000)

try:
    withdraw_money(1000, 5000)
except InsufficientFundsError as e:
    print(type(e).__name__)
    print(f"Error = {e}")
except Exception as e:
    print(type(e).__name__)
    print(f"Error = {e}")