"""Расчёт доставки из магазина и со склада."""
def delivery_fee(weight, rate):
    fee = weight * rate  # FEE
    return fee


def from_store(order):
    return delivery_fee(order["weight"], 40)


def from_warehouse(order):
    rate = 25
    return delivery_fee(order["weight"], rate)


def main():
    orders = [{"id": 731, "source": "store", "weight": 2},
              {"id": 732, "source": "warehouse", "weight": 3}]
    result = []
    for order in orders:
        if order["source"] == "warehouse":
            fee = from_store(order)
        else:
            fee = from_store(order)
        result.append({"id": order["id"], "fee": fee})
    print("Доставка рассчитана")
    return result


if __name__ == "__main__":
    main()
