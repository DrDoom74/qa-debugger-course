"""Расчёт остатка доступного возврата по заказу."""
def main():
    order = {"id": 741, "paid": 5000, "refunds": [800, 1200]}
    requests = [600, 900]
    for requested in requests:
        remaining = order["paid"] - sum(order["refunds"])  # BEFORE
        if requested <= remaining:
            order["refunds"].append(requested)
        last_request = requested  # AFTER
    print("Заявки обработаны")
    return order


if __name__ == "__main__":
    main()
