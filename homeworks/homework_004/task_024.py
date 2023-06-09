# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

n = int(input('Введите число кустов: '))
list_n = list()

for i in range(n):
    list_n.append(int(input('Количество ягод на кусте: ')))

sum = max_sum = list_n[-2] + list_n[-1] + list_n[0]

for i in range(1, n):
    sum = sum - list_n[i - 3] + list_n[i]
    max_sum = sum if (sum > max_sum) else max_sum

print(max_sum)