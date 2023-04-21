# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Введите n: '))
m = int(input('Введите m: '))
list_n = list(n)
list_m = list(m)

for i in range(n):
    list_n.append(int(input('Введите число первого множества: ')))
for i in range(m):
    list_m.append(int(input('Введите число второго множества: ')))
# list_n = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
# list_m = [3, 6, 9, 12, 15, 18]

print(*sorted(set(list_n).intersection(set(list_m))))