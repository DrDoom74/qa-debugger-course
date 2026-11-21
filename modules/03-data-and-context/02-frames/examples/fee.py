"""Расчёт комиссии с передачей ставки через две функции."""
DEFAULT_RATE = 5


def calculate_fee(amount, rate):
    fee = amount * rate // 100  # FEE
    return fee


def prepare_payment(order):
    amount = order["amount"] - order["discount"]
    rate = order["rate"]
    fee = calculate_fee(amount, rate)  # CALL_FEE
    return amount - fee


def main():
    order = {"id": 721, "amount": 3000, "discount": 200, "rate": 4}
    rate = DEFAULT_RATE
    payable = prepare_payment(order)  # CALL_PAYMENT
    print("Выплата подготовлена")  # FINISH
    return payable


if __name__ == "__main__":
    main()
