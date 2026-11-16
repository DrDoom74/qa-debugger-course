"""Подготовка итоговой сводки по заказам."""
def main():
    amounts = [1200, 700, 1800, 900]
    total = 0  # START
    for amount in amounts:
        total = total + amount  # INSIDE_LOOP
    commission = total * 5 // 100  # SUMMARY
    payable = total - commission
    print("Сводка подготовлена")  # FINISH
    return payable


if __name__ == "__main__":
    main()
