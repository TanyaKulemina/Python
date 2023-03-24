# Задача. Проверка палиндрома. Напишите функцию, которая проверяет, является ли строка палиндромом
# (то есть читается одинаково справа налево и слева направо) с использованием рекурсии.


def palindrom(n):
    if len(n) <= 1:
        return ''
    else:
        if n[0] == n[len(n) - 1]:
            palindrom(n[1:len(n) - 1])
        else:
            return 'no'
    return 'yes'


string = input("Введите строку для проверки: ")
print(palindrom(string))
