# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2

n = int(input('Введите N: '))
list = []
for i in range(n):
    list.append(int(input('Введите целое число: ')))

x = int(input('Введите число X: '))
countX = 0

for el in list:
    if el == x:
        countX += 1

print(f'Число ({x}) встречается {countX} раз.')
