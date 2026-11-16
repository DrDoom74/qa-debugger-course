"""Применение скидки на весь заказ."""
def calculate_amount(price, quantity, discount):
    discounted_price = price - discount  # CALC_START
    amount = discounted_price * quantity
    return amount  # CALC_RETURN


def main():
    order = {"id": 501, "price": 750, "quantity": 4, "discount": 200}
    amount = calculate_amount(order["price"], order["quantity"], order["discount"])  # CALL_CALC
    receipt = {"id": order["id"], "amount": amount}  # RECEIPT
    print("Счёт подготовлен")
    return receipt


if __name__ == "__main__":
    main()
