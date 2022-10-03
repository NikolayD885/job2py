# Реализуйте алгоритм перемешивания списка.

import random

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Оригинальный список : " + str(listA))

for i in range(len(listA)-1, 0, -1):
    j = random.randint(0, i + 1)
    listA[i], listA[j] = listA[j], listA[i]

print("Перемешенный список : " + str(listA))
