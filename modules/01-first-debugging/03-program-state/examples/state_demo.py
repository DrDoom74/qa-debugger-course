"""Списание стоимости покупки с баланса, суммы в рублях."""
def main():
    balance = 2500
    purchase = 700
    balance = balance - purchase  # BEFORE_DEBIT
    receipt = {"spent": purchase, "remaining": balance}  # AFTER_DEBIT
    print(f"Остаток: {balance}")
    return receipt


if __name__ == "__main__":
    main()
