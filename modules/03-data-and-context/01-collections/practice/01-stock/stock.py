"""Резервирование товара на выбранном складе."""
def main():
    stock = {"west": {"BOOK-1": 12, "PEN-4": 20},
             "east": {"BOOK-1": 9, "PEN-4": 15}}
    requests = [{"id": 711, "warehouse": "east", "sku": "BOOK-1", "quantity": 3},
                {"id": 712, "warehouse": "west", "sku": "PEN-4", "quantity": 4}]
    for request in requests:
        warehouse = stock["west"]  # SELECT
        sku = request["sku"]
        warehouse[sku] = warehouse[sku] - request["quantity"]
        processed_id = request["id"]  # OBSERVE
    print("Резервирование завершено")
    return stock


if __name__ == "__main__":
    main()
