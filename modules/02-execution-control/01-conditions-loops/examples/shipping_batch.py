"""Стоимость доставки для небольшой партии заказов."""
def main():
    orders = [
        {"id": 201, "amount": 2400, "discount": 0},
        {"id": 202, "amount": 3200, "discount": 400},
        {"id": 203, "amount": 3600, "discount": 300},
    ]
    delivery_total = 0
    for order in orders:
        payable = order["amount"] - order["discount"]  # ORDER_START
        if payable >= 3000:  # CHECK_LIMIT
            delivery = 0
        else:
            delivery = 250
        delivery_total = delivery_total + delivery  # ADD_DELIVERY
        last_order_id = order["id"]  # ORDER_DONE
    print("Расчёт доставки завершён")  # BATCH_DONE
    return delivery_total


if __name__ == "__main__":
    main()
