import random


def get_numbers_ticket(min, max, quantity):  # функція на генерацію виграшної комбінації
    win_number = []      # створюємо порожній список\

    # Якщо мінімальне число не відповідає параметрам задачі повернути порожній список
    # (обмеження по максимуму в задачі не вказано)
    if min <= 0 or min > 999:
        pass

    # Якщо максимальне число не відповідає параметрам задачі повернути порожній список
    elif max <= min or max > 1000:
        pass

    # Якщо кількість елементів унікального списку задана невірно повернути поржній список
    elif quantity > max - min or quantity <= 0:
        pass

    else:
        while len(win_number) != quantity:     # цикл працює поки список не набере потрібну кількість комбінацій
            number = random.randrange(min, max + 1)    # Генерація випадкового числа в заданих межах

            if win_number.count(number) == 0:   # Якщо згенерованого числа ще не має в списку то додати його
                win_number.append(number)

    return win_number     # Повернути список з функції


print(get_numbers_ticket(10, 15, 5))