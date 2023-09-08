# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import random

x = random.randint(0, 1000)
y = random.randint(0, 1000)

multXY = x * y
print(f'Multiple of numbers is:',multXY, end=', ')
sumXY = x + y
print(f'sum of numbers is:',sumXY, end='.\n')

b=0
for i in range(0,1000):
    if sumXY*i - i*i == multXY:
        b = i
        break
# i=0
# while sumXY*i - i*i != multXY:
#     i+=1
# else: b=i

print(f'Those numbers are {b} and {sumXY-b}')


