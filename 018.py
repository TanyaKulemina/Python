# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

import random
n = int(input("Введите количество элементов в массиве: "))
list = list()
for i in range(n):
    list.append(random.randint(1,10))
print(*list)

x = int(input("Введите число, для которого найдем ближайшее: "))
min = abs(x - list[0])

for i in list:
    if abs(x - i) < min:
        min = abs(x - i)
        result = i

print(result)
