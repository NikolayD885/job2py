# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

number = int(input('Введите число :'))


def ArrayDigitsMultiplier(n):
    listA = []
    for i in range(1, n + 1):
        listA.append((1+1/i)**i)
    return listA


print(ArrayDigitsMultiplier(number))
print(sum(ArrayDigitsMultiplier(number)))
