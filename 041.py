# **Задача 41.**  Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 5 —> 1 2 3 4 5
# Вывод: 0
# Ввод: 5 —> 1 5 1 5 1
# Вывод: 2

from random import randint 

n = int(input("Введите количество элементов списка: "))
list_1 = [randint(1, 10) for i in range(n)]
print(*list_1)
result = 0

for i in range(1, len(list_1)-1):
    if list_1[i-1] < list_1[i] > list_1[i+1]:
        result += 1

print(result)

