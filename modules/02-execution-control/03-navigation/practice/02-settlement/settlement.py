"""Подготовка выплаты по проведённым операциям."""
def main():
    payments = [{"amount": 1800, "status": "done"},
                {"amount": 900, "status": "held"},
                {"amount": 2400, "status": "done"},
                {"amount": 1300, "status": "done"}]
    gross = 0  # START
    for payment in payments:
        if payment["status"] == "done":  # CHECK_PAYMENT
            gross = gross + payment["amount"]
    fee = gross * 4 // 100  # FEE
    payable = gross - fee
    report = {"gross": gross, "fee": fee, "payable": payable}  # REPORT
    print("Выплата подготовлена")
    return report


if __name__ == "__main__":
    main()
