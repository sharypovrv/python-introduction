# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first = int(input('Первый элемент: '))
d = int(input('Коэффициент: '))
quantity = int(input('Количество элементов: '))

arr = list()

for i in range(quantity):
    arr.append(first + d * i)

print(arr)