# Високосный год

def is_year_leap():
    if year % 4 == 0:
        print(f'{True} Это високосный год')

    else:
        print(f'{False} Это не високосный год')


year = int(input('Введите год для проверки: \n'))
is_year_leap()
