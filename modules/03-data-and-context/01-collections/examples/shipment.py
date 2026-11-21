"""Подготовка отправления с несколькими товарными позициями."""
def main():
    shipment = {
        "id": 701,
        "recipient": {"city": "Пермь", "pickup": "P-12"},
        "items": [{"sku": "BOOK-1", "quantity": 2},
                  {"sku": "PEN-4", "quantity": 5}],
    }
    selected = shipment["items"][1]
    selected["quantity"] = selected["quantity"] - 1  # ADJUST
    label = {"id": shipment["id"], "city": shipment["recipient"]["city"]}  # LABEL
    print("Отправление подготовлено")
    return label


if __name__ == "__main__":
    main()
