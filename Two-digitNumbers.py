# Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в 
# одну строчку через пробел.

# 23 345 567 1

print(*list(filter(lambda x: len(x) == 2, input("Введите текст: ").split())))


# решение 2
# print(*list(filter(lambda x: 9<x<100, list(map(lambda x: int(x),input("Введите текст: ").split())))))


# решение 2 подробно
# list_1 = "23 345 567 1".split()
# print(list_1)

# list_1 = list(map(lambda x: int(x),list_1))
# print(list_1)

# list_1 = list(filter(lambda x: 9<x<100, list_1))
# print(list_1)


