"""Расчёт заказа: доставка зависит от суммы после скидки."""
def main():
    order = {"id": 103, "price": 1550, "quantity": 2, "discount": 300}
    price = order["price"]
    quantity = order["quantity"]
    subtotal = price * quantity
    discount = order["discount"]
    discounted_total = subtotal - discount
    free_delivery_from = 3000
    delivery = 250
    if subtotal >= free_delivery_from:
        delivery = 0
    total = discounted_total + delivery
    print(f"К оплате: {total}")  # FIRST_STOP
    return total


if __name__ == "__main__":
    main()
