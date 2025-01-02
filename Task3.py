import re


raw_numbers = [     # Задані номери
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
deffect_number = []    # Список для прийому винятків які програма не обробляє


def normalize_phone(number):     # Функція форматування номерів під 1 формат
    waste = r"\D+"
    clean_number = re.sub(waste, "", number)    # Видаляємо лишні символи і пробіли з рядків

    if len(clean_number) == 10:   # якщо номер без коду країни то додати "+38" на початок
        clean_number = "+38" + clean_number
        return clean_number

    elif len(clean_number) == 12:    # якщо номер з кодом країни то додати "+" на початок
        clean_number = "+" + clean_number
        return clean_number

    else:     # якщо номер буде виодити за межі програми додати його в список для апгрейду програми
        deffect_number.append(clean_number)


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:\n", sanitized_numbers)
print("Винятки програми для абгрейду:", deffect_number)