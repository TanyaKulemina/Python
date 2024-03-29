# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10 в пятой степени
# Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 300 делители: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 25, 30, 50, 60, 75, 100, 150
# Вывод: 220 (делители - 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110 = 284) 
# 284 Список делителей для 284: 1, 2, 4, 71 и 142, — и сумма равна 220.

def summa_del(n):
    summa = 0
    for i in range(1, n):
        if n % i == 0:
            summa += i
    return summa

k = 300
for i in range(1, k):
    j = summa_del(i)
    if i == summa_del(j) and i != j:
        print(i, j)