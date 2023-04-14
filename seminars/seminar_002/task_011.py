# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# Вариант 1 (мой)
number = int(input('Введите A: '))
fib1 = 0
fib2 = 1
fib = fib1 + fib2
i = 3
n = -1
if number == 0:
    n = 1
elif number == 1:
    n = 2
else:
    while number >= fib:
        i += 1
        fib1 = fib2
        fib2 = fib
        fib += fib1
        # print(fib)
        if (number == fib):
            n = i
print(n)

# Вариант 2 (с семинара)
if number == 0:
    print(1)
else:
    fibPrev, fibNext = 0, 1
    m = 2
    while number >= fibNext:
        if number == fibNext:
            print(m)
            break
        fibPrev, fibNext = fibNext, fibNext + fibPrev
        m += 1
    else:
        print(-1)