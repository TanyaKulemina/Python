# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств

import random
n = int(input("Введите число элементов в первом множестве: "))
m = int(input("Введите число элементов во втором множестве: "))
list1 = list()
list2 = list()

for i in range(n):
    list1.append(random.randint(1,10))
set1 = set(list1)
print(*list1)


for j in range(n):
    list2.append(random.randint(1,10))
set2 = set(list2)
print(*list2)

i = set1.intersection(set2)
print(*i)
print(*sorted(i))
