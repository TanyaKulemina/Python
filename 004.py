# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

summa = int(input('Введите число: '))
if summa % 666 == 0:
    p = summa // 6
    s = p
    k = 4 * s
    print(p, k, s)
else:
    print("Такое число журавликов не могло получиться")
