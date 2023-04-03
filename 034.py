# **Задача 34:** Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод: Парам пам-пам


# решение через функцию
def count_vowels(list_1, list_2):
    list_3 = []
    for i in range(len(list_1)):
        list_3.append(0)
        for j in list_2:
            list_3[i] += list_1[i].count(j)
    return list_3

def compare_words(list_4, a, b):
    for i in range(len(list_4) - 1):
        if list_4[i] != list_4[i + 1]:
            return a
        return b

list_of_words = input("Введите текст: ").split()
list_of_vowels = ['а', 'ы', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и']

list_result = count_vowels(list_of_words, list_of_vowels)
print(compare_words(list_result, "Пам парам", "Парам пам-пам"))



# решение через циклы
# list_of_words = input("Введите текст: ").split()
# list_of_vowels = ['а', 'ы', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и']
# list_result = []

# for i in range(len(list_of_words)):
#     list_result.append(0)
#     for j in list_of_vowels:
#         list_result[i] += list_of_words[i].count(j)

# print(list_result)
# for i in range(len(list_result) - 1):
#     if list_result[i] != list_result[i + 1]:
#         res = "Пам парам"
#     else:
#         res = "Парам пам-пам"

# print(res)


            



