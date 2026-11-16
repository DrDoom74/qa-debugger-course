"""Расчёт упаковки и её стоимости."""
def count_boxes(quantity, capacity):
    boxes = quantity // capacity  # BOXES_START
    return boxes  # BOXES_RETURN


def packaging_cost(quantity, capacity, box_price):
    boxes = count_boxes(quantity, capacity)  # CALL_BOXES
    cost = boxes * box_price  # COST
    return cost


def main():
    quantity = 14
    capacity = 6
    box_price = 90
    cost = packaging_cost(quantity, capacity, box_price)  # CALL_COST
    report = {"quantity": quantity, "packaging_cost": cost}  # REPORT
    print("Упаковка рассчитана")
    return report


if __name__ == "__main__":
    main()
