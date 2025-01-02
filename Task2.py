import random


min_value = None
max_value = None
quantity = None


while type(min_value) != int:   # Перевірка на правильність введення початку лотереї
    try:    # якщо введуть ціле число то
        min_value = int(input(f"{"_"*30}\nEnter the minimum lottery value"))

        if min_value <= 0:     # якщо початок лотереї менше 0 включно прохання ввести початок заново
            print(f"{"_"*30}\nMinimum lottery value cannot be less than 0")
            min_value = None
        # Тут я б ще додав обмеження на верхній діапазон але в задачі такого вказано не було,
        # можете прийняти за помилку

        #elif min_value >= 998:      # Але вирішив що якщо потрібна всетаки то нехай полежить тут)
            #print(f"{"_" * 30}\nMinimum lottery value cannot be more than 998")
            #min_value = None

    except:    # Якщо ввели не число або не ціле число, прохання ввести коректні данні
        print(f"{"_"*30}\nInvalid value, try again")
        min_value = None


while type(max_value) != int:       # Перевірка на правильність введення максимального порогу лотереї
    try:    # якщо введуть ціле число
        max_value = int(input(f"{"_"*30}\nEnter the maximum lottery value"))

        if max_value <= min_value:    # Прохання ввести заново якщо введений верхній порог менше нижнього
            print(f"{"_" * 30}\nMaximum lottery value cannot be less than minimum value")
            max_value = None

        elif max_value > 1000:      # Прохання ввести заново якщо верхній порог бідьше 1000
            print(f"{"_" * 30}\nMaximum lottery value cannot be more then 1000")
            max_value = None

    except:      # Якщо ввели не число або не ціле число, прохання ввести коректні данні
        print(f"{"_" * 30}\nInvalid value, try again")
        max_value = None


while type(quantity) != int:     # Перевірка на правильність введеня кількості виграшних позицій
    try:
        quantity = int(input(f"{"_"*30}\nEnter the number of winning positions"))

        if quantity <= 0:       # Якщо кількість виграшних позицій менше або дорівнює 0 прохання переввести
            print(f"{"_" * 30}\nThere must be at least one winning number in the lottery")
            quantity = None

        elif quantity >= max_value - min_value:      # Якщо кількість позицій перевищує діапазон виграшних
                                                     # номерів прохання переввести данні
            print(f"{"_" * 30}\nThere cannot be more winning positions than positions in total")
            quantity = None

    except:     # Якщо ввели не число або не ціле число, прохання ввести коректні данні
        print(f"{"_" * 30}\nInvalid value, try again")
        quantity = None


def get_number_ticket(min_value, max_value, quantity):  # функція на генерацію виграшної комбінації
    win_number = []      # створюємо порожній список
    while len(win_number) != quantity:     # цикл працює поки список не набере потрібну кількість комбінацій
        number = random.randrange(min_value, max_value + 1)    # Генерація випадкового числа в заданих межах

        if win_number.count(number) == 0:   # Якщо згенерованого числа ще не має в списку то додати його
            win_number.append(number)
    return win_number     # Повернути список з функції


print(get_number_ticket(min_value, max_value, quantity))