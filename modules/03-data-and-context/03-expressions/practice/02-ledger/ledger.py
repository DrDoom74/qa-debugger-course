"""Сверка суммы возвратов с исходной оплатой."""
def main():
    paid = 3000
    refunds = [400]
    requests = [{"id": 751, "amount": 500},
                {"id": 752, "amount": 700},
                {"id": 753, "amount": 900},
                {"id": 754, "amount": 300}]
    for request in requests:
        remaining = paid - sum(refunds)  # BEFORE
        if request["amount"] <= remaining:
            refunds.append(request["amount"])
            if request["id"] == 753:
                refunds.append(request["amount"])
        last_id = request["id"]  # AFTER
    print("Возвраты обработаны")
    return refunds


if __name__ == "__main__":
    main()
