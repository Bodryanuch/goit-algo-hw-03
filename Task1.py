from datetime import datetime


given_date = "2020-10-09"


def get_days_from_today(date):
    today = datetime.now()  # Сьогоднішня дата
    checked_date = datetime.strptime(date, "%Y-%m-%d")       # Переведення рядка в об'єкт дататайм
    difference_day = today.toordinal() - checked_date.toordinal()      # Дізнаємося різницю в днях
    return difference_day     # Повертаємо результат


print(get_days_from_today(given_date))