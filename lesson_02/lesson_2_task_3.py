# Площадь квадрата

import math


def square(lenght_of_side_input):
    integer_value = math.ceil(lenght_of_side_input)
    square_area = integer_value ** 2

    print(f'Площадь квадрата: {square_area}')


lenght_of_side_input = float(input('Введите значение: '))
square(lenght_of_side_input)
