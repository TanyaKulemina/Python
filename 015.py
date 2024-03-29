# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random
n = int(input("Введите количество арбузов: "))
count = 0
weight = 0
max = 0
min = 10
while count < n:
    a = random.randint(1,10)
    print(a)
    if a > max:
        max = a
    elif a < min:
        min = a
    count = count + 1
print(f"Самый легкий арбуз {min}кг. Самый тяжелый арбуз {max}кг.")

