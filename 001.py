# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# 0,56 -> 11

number = float(input('Введите вещественное число :'))
summa = 0
number = abs(number)


def DigitAfterDotCounter(num: float):
    count = 0
    div = 1
    while True:
        if not (num*div == int(num*div)):
            count += 1
            div *= 10
        else:
            break
    return count


num = number * (10**DigitAfterDotCounter(number))

while num != 0:
    summa += num % 10
    num //= 10

print(int(summa))
