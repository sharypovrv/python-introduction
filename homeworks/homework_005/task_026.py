# Задача 26:  Посчитать факториал (произведение 1 до N)
# и треугольное число (сумма чисел от 1 до N)
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def get_triangular_number(n):
    if n == 1:
        return 1
    return n + get_triangular_number(n - 1)

n = int(input("N = "))
print(f"fact({n}) = {fact(n)}")
print(f"triangular_number({n}) = {get_triangular_number(n)}")