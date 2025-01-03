import random


min_value = 1
max_value = 49
quantity = 6


def get_number_ticket(min_value, max_value, quantity):  # функція на генерацію виграшної комбінації
    win_number = []      # створюємо порожній список
    while len(win_number) != quantity:     # цикл працює поки список не набере потрібну кількість комбінацій
        number = random.randrange(min_value, max_value + 1)    # Генерація випадкового числа в заданих межах

        if win_number.count(number) == 0:   # Якщо згенерованого числа ще не має в списку то додати його
            win_number.append(number)
    return win_number     # Повернути список з функції


print(get_number_ticket(min_value, max_value, quantity))