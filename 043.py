# **Задача 43.** Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3
# Вывод:
# 2

n = int(input("Введите число элементов: "))
list_1 = []

for i in range(n):
    list_1.append(int(input("Введите элемент: ")))

print(*list_1)

count = 0 
i = 0 
while i < len(list_1) - 1: 
    j = i + 1 
    flag = True 
    while j < len(list_1) and flag: 
        if list_1[i] == list_1[j]: 
            count += 1 
            list_1.pop(j) 
            flag = False 
        j += 1 
    i += 1 
 
print(count)

# count = 0
# i = 0
# while i < len(list_1):
#     j = i + 1
#     while j < len(list_1):
#         print(i, j)
#         if list_1[i] == list_1[j]:
#             list_1.pop(j)
#             list_1.pop(i)
#             print(list_1)
#             count += 1
#         j += 1
#     i += 1

# print(count)