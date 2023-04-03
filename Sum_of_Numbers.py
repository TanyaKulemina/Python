# Напишите программу, которая принимает на
# вход вещественное число и показывает сумму его цифр.
# Пример:
# -6782 -> 23
# -0,56 -> 11

import re

n = re.sub("[-,]","",input("Введите число: "))

result = sum(map(lambda x: int(x), n))
# for i in range(len(m)):
#     result += int(m[i])

print(result)