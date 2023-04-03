# Вводится натуральное число N. 
# С помощью list comprehension сформировать двумерный список размером N x N, 
# состоящий из нулей, а по главной диагонали - единицы. 
# Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы 
# до ее нижнего правого угла). 
# Результат вывести в виде таблицы чисел как показано в примере ниже.
# Sample Input: 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

num = int(input("Введите натуральное число N: ")) 
for a in range(num): 
    list_1 = [[1 if i == a else 0 for i in range(0, num)] for a in range(num)] 
    print(*list_1)


# def matrix(num):
#     for i in range(1, num + 1):
#         list_1 = []
#         row = i
#         for j in range(1, num + 1):
#             if len(list_1) == row - 1:
#                 list_1.append(1)
#             else:
#                 list_1.append(0)
#         print(*list_1)

# n = int(input("Введите число: "))
# matrix(n) 





