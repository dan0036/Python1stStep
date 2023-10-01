# Задача 34:  Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “
# Пам парам”, если с ритмом все не в порядке.
import random

set_vowel = "йуеаоэёяиюы"
verse = input('Введите стихотворение: ')
# print(set_vowel)
# print(list(verse.split(' ')))

list_temp = []
for i in range(len(list(verse.split(' ')))):
    list_temp.append(0)
    for j in list(verse.split(' '))[i]:
        if j in set_vowel:
            list_temp[i] += 1
# print(list_temp)

if list_temp == list(filter(lambda x: x == list_temp[0], list_temp)):
    print('Парам пам-пам')
else:
    print('Пам парам')

