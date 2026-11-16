"""Импорт записей с отбрасыванием дублей и невалидных сумм."""
def main():
    rows = [{"id": 601, "amount": 1200}, {"id": 602, "amount": 0},
            {"id": 601, "amount": 1200}, {"id": 603, "amount": 1800},
            {"id": 604, "amount": 700}, {"id": 605, "amount": -100}]
    seen = []  # START
    accepted = 0
    rejected = 0
    total = 0
    for row in rows:
        if row["id"] in seen or row["amount"] <= 0:  # ROW
            rejected = rejected + 1
            continue
        seen.append(row["id"])
        accepted = accepted + 1
        total = total + row["amount"]
    report = {"accepted": accepted, "rejected": rejected, "total": total}  # REPORT
    print("Импорт завершён")
    return report


if __name__ == "__main__":
    main()
