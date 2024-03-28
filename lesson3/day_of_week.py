# Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. Якщо номер дня недійсний 
#(менше 1 або більше 7), виведіть повідомлення про помилку.


import random

random_number = random.randint(1,10)


day_of_week = {
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday",
}


if random_number < 8 and random_number > 0:
    random_string = str(random_number)
    print(day_of_week.get(random_string))
else:
    print("Помилка")
