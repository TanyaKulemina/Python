# Задача №17. Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# list = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list)))

# list = list(input("Введите числа через пробел: ").split(" "))
# print(len(set(list)))

list = input("Введите числа через пробел: ").split(" ")
newList = []
for i in list:
    if i not in newList:
        newList.append(i)
        count = len(newList)
print(count)