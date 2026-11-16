"""Сводка выручки по оплаченным заказам."""
def main():
    orders = [
        {"id": 301, "status": "paid", "amount": 1800, "discount": 100},
        {"id": 302, "status": "cancelled", "amount": 900, "discount": 0},
        {"id": 303, "status": "paid", "amount": 2600, "discount": 200},
        {"id": 304, "status": "paid", "amount": 1200, "discount": 100},
    ]
    revenue = 0
    for order in orders:
        if order["status"] == "paid":  # ORDER_START
            net = order["amount"] - order["discount"]
            revenue = revenue + net
        else:
            revenue = 0
        last_order_id = order["id"]  # ORDER_DONE
    print("Сводка выручки подготовлена")
    return revenue


if __name__ == "__main__":
    main()
