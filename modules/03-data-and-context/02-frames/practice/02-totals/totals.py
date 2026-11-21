"""Последовательное начисление оплаченных заказов."""
def add_order(total, amount):
    total = total + amount
    return total  # RETURN_TOTAL


def main():
    total = 1000
    amounts = [700, 900]
    for amount in amounts:
        total = add_order(total, amount)  # CALL_ADD
    print("Начисление завершено")
    return total


if __name__ == "__main__":
    main()
