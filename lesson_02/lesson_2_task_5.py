# Месяц - сезон

def month_to_season(num_of_month):
    if num_of_month == 3 or num_of_month == 4 or num_of_month == 5:
        print('Весна')

    elif num_of_month == 6 or num_of_month == 7 or num_of_month == 8:
        print('Лето')

    elif num_of_month == 9 or num_of_month == 10 or num_of_month == 11:
        print('Осень')

    elif num_of_month == 12 or num_of_month == 1 or num_of_month == 2:
        print('Зима')

    else:
        print("Такого месяца не существует! Введите значение от 1 до 12")


num_of_month = int(input('Введите номер месяца: '))
month_to_season(num_of_month)
