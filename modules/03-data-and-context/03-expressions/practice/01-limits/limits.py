"""Проверка возможности нового возврата."""
def main():
    payment = {"paid": 4200, "refunds": [700, 1100, 400]}
    requested = 2100
    allowed = requested <= payment["paid"]  # CHECK
    result = {"allowed": allowed, "requested": requested}  # RESULT
    print("Проверка завершена")
    return result


if __name__ == "__main__":
    main()
