"""Подготовка счёта за канцелярские товары, суммы в рублях."""
def main():
    order = {"id": 701, "price": 480, "quantity": 4, "discount": 320}
    subtotal = order["price"] * order["quantity"]
    payable = subtotal - order["discount"]
    receipt = {"order_id": order["id"], "amount": payable}  # INVOICE_STOP
    print("Счёт подготовлен")
    return receipt


if __name__ == "__main__":
    main()
