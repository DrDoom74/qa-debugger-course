"""Подготовка логина пользователя для сохранения."""
def main():
    raw_login = "  QA.Student  "
    stripped_login = raw_login.strip()
    normalized_login = stripped_login.lower()
    profile = {"login": normalized_login, "active": True}  # PROFILE_STOP
    print("Профиль подготовлен")
    return profile


if __name__ == "__main__":
    main()
