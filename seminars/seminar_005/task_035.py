# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n (само число)
# Input: 5
# Output: yes

def is_simple(in_number):
    for i in range(2, int(in_number**0.5 + 1)):
        if in_number % i == 0:
            return False
    return True

number = int(input('Введите число: '))
# for i in range(number):
#     print(f"{i} => {is_simple(i)}")
print(is_simple(number))