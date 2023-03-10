# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите число: '))
summa = 0
while number > 0:
	x = number % 10
	summa = summa + x
	number = number // 10
print(summa) 