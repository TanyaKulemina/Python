# **Задача 30:** Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. 
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a = int(input("Введите первый элемент: "))
b = int(input("Введите разность: "))
c = int(input("Введите количество элементов: "))

list_1 = []

n = range(a, a + b * c, b) # первое число, последнее число не включая, шаг
for i in n:
    list_1.append(i)
    
print(*list_1)