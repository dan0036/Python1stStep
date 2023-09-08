# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
from math import pow
import random

n = random.randint(0, 10000)
print(f'Upper limit is {n}')

k=1
while k < n/2:
   k*=2
   print(k, end=' ')
