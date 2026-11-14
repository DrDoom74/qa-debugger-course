"""Подготовка отгрузки товара со склада."""
def main():
    stock = 24
    quantity = 7
    reserved = quantity
    available = stock
    available = available - reserved  # BEFORE_RESERVE
    shipment = {"quantity": reserved, "remaining": available}  # AFTER_RESERVE
    print("Отгрузка подготовлена")
    return shipment


if __name__ == "__main__":
    main()
