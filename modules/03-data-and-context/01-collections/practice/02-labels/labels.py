"""Подготовка меток обычной и срочной отправки."""
def main():
    template = ["paid", "packed"]
    standard = template
    express = standard
    express.append("priority")  # ADD_LABEL
    documents = {"standard": standard, "express": express}  # DOCUMENTS
    print("Документы подготовлены")
    return documents


if __name__ == "__main__":
    main()
