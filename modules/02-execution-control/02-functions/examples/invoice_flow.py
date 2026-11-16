"""Расчёт счёта с отдельными функциями цены и доставки."""
def calculate_net(price, quantity, discount):
    subtotal = price * quantity  # NET_START
    net = subtotal - discount
    return net  # NET_RETURN


def delivery_cost(net):
    if net >= 3000:
        return 0
    return 250


def main():
    price = 800
    quantity = 4
    discount = 300
    net = calculate_net(price, quantity, discount)  # CALL_NET
    delivery = delivery_cost(net)  # CALL_DELIVERY
    total = net + delivery  # AFTER_DELIVERY
    print("Счёт подготовлен")  # INVOICE_DONE
    return total


if __name__ == "__main__":
    main()
