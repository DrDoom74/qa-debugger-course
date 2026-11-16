"""Последовательное резервирование остатков для заявок."""
def main():
    requests = [{"id": 401, "quantity": 5}, {"id": 402, "quantity": 8},
                {"id": 403, "quantity": 7}, {"id": 404, "quantity": 2}]
    available = 20
    accepted = []
    for request in requests:
        quantity = request["quantity"]  # REQUEST_START
        if quantity < available:
            available = available - quantity
            accepted.append(request["id"])
        last_request_id = request["id"]  # REQUEST_DONE
    print("Резервирование завершено")
    return available, accepted


if __name__ == "__main__":
    main()
