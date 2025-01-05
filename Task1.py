from datetime import datetime
import re

given_date = ("2020-02-02")


def get_days_from_today(date:str):
    try:
        today = datetime.now()  # Сьогоднішня дата
        checked_date = datetime.strptime(date, "%Y-%m-%d")       # Переведення рядка в об'єкт дататайм
        difference_day = today.toordinal() - checked_date.toordinal()      # Дізнаємося різницю в днях
        return difference_day     # Повертаємо результат
    except ValueError:      # функція нічого не робить при некоректно введеній або неіснуючій даті
        pass
    except TypeError:       # функція нічого не робить якщо прийняті нею данні невірного типу
        pass


print(get_days_from_today(given_date))