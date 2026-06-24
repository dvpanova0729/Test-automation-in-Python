# Фильтр

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            new_i = 'Fizz'
            print(new_i)

        elif i % 5 == 0 and i % 3 != 0:
            new_i = 'Buzz'
            print(new_i)

        elif (i % 3 == 0) and (i % 5 == 0):
            new_i = 'FizzBuzz'
            print(new_i)

        else:
            print(i)


n = int(input('Введите число: '))
fizz_buzz(n)
