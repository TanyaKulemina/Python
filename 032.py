# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint 

list_1 = [randint(-15, 15) for i in range(20)]
print(list_1)
list_2 = []

min = int(input("Введите минимальное число интервала: "))
max = int(input("Введите максимальное число интервала: "))

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        list_2.append(i)

print(list_2)

