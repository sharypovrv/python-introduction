# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число 
# А в целую степень B с помощью рекурсии.

def func(a, b):
        return 1 if (b == 0) else a * func(a, b - 1)

a = int(input('a = '))
b = int(input('b = '))
print(func(a, b))