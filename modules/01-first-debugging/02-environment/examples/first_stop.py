"""Стоимость комплекта с доставкой, суммы в рублях."""
def main():
    price = 450
    quantity = 3
    subtotal = price * quantity
    delivery = 200
    total = subtotal + delivery
    print(f"К оплате: {total}")  # FIRST_STOP
    return total


if __name__ == "__main__":
    main()
