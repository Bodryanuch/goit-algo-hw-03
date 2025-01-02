from datetime import datetime#, timedelta
import re


today = datetime.now().date()
given_date = input("enter the date in the format year-month-day (YYYY-MM-DD):")
format_date = r"\d{4}-\d{2}-\d{2}"    # шаблон відповідності введеного формату дати


def checked_date(date):      # Функція обробки вийнятків
    checked_given_date = None
    clone_date = date

    while checked_given_date == None:    # цикл який запитує введення даних доки данні не будуть коректними
        match = re.search(format_date, clone_date)

        if match == None:      # Якщо не відповідає формату введення данних то
            print(f"{"_" * 30}\nInvalid input format\n{"_" * 30}")
            clone_date = input("enter the date in the format year-month-day (YYYY-MM-DD):")

        else:
            try:    # Якщо формат введення дати правельний то переводимо рядок в об'єкт datetime
                checked_given_date = datetime.strptime(match.group(), "%Y-%m-%d")
            except:    # На випадок якщо задана дата не існує
                print(f"{"_" * 30}\nDate does not exist\n{"_" * 30}")
                clone_date = input("enter the date in the format year-month-day:")

    return checked_given_date.date()


def get_days_from_today(date):     # функція різниці в днях між датами
    difference_day = checked_date(date).toordinal() - today.toordinal()

    if difference_day < 0:    # Якщо дата вже пройшла то вивести:
        print(f"{abs(difference_day)} days have passed since the given date")

    elif difference_day > 0:     # Якщо дата в майбутньому то вивести:
        print(f"There are {difference_day} days left until the given date")

    else:    # якщо дата сьогодні то вивести:
        print("today's date is entered")

get_days_from_today(given_date)