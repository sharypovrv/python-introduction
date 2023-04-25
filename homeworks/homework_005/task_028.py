# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4 

def get_sum(a, b):
    if a > 0:
        return get_sum(a - 1, b) + 1
    elif a < 0:
        return get_sum(a + 1, b) - 1
    elif b > 0:
        return get_sum(0, b - 1) + 1
    elif b < 0:
        return get_sum(0, b + 1) - 1
    return 0
    
a = int(input('a = '))
b = int(input('b = '))
print(get_sum(a, b))