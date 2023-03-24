# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

def change(list):
    maximum = max(list)
    minimum = min(list)

    for i in range(len(list)):
        if list[i] == maximum:
            list[i] = minimum

n = int(input("Введите количество оценок: "))
list = [randint(1, 5) for i in range(n)]
print(*list)
change(list)
print(*list)


