# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
import random
n = int(input('Enter a positive integer: '))
heads, tails = 0, 0
for i in range(0, n):
    temp = random.randint(0,1)
    print(temp, end=' ')
    if temp == 1: heads += 1
    else: tails += 1
if tails < heads: print(f'--heads are more up, and only {tails} turns of tails are needed.')
elif tails > heads: print(f'--tails are more up, and only {heads} turns of heads are needed.')
else: print(f'--no matter heads or tails, turn {tails} times')
