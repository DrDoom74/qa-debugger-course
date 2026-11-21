"""Сверка заказа и данных для чека."""
def check_receipt(receipt):
    expected = receipt["quantity"] * receipt["price"]
    difference = receipt["amount"] - expected  # CHECK_RECEIPT
    return difference == 0


def prepare(order):
    receipt = {"quantity": order["quantity"], "price": order["price"],
               "amount": order["quantity"] * order["price"],
               "discount": order["discount"]}
    return check_receipt(receipt)


def main():
    order = {"id": 761, "quantity": 3, "price": 800, "discount": 200}
    valid = prepare(order)
    print("Сверка завершена")
    return valid


if __name__ == "__main__":
    main()
