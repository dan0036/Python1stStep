# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Enter a1 member: '))
n = int(input('Enter n quantity of members: '))
d = int(input('Enter d - step "+": '))

print(list_1 := [a1 + (n-1)*d for n in range(1, n+1)])


