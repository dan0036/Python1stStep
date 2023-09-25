# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
import random

print(list_1 := [random.randint(0, 9) for _ in range(10)])
min = 2
max = 7

print(list_idx := [i for i in range(len(list_1)) if min < list_1[i] < max])