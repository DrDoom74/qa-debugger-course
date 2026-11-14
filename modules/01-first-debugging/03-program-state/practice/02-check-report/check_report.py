"""Сводка результатов выполненных проверок."""
def main():
    counts = {"passed": 18, "failed": 3, "skipped": 2}
    passed = counts["passed"]
    failed = counts["failed"]
    skipped = counts["skipped"]
    total = passed + failed
    report = {"total": total, "failed": failed}  # REPORT_STOP
    print("Отчёт подготовлен")
    return report


if __name__ == "__main__":
    main()
