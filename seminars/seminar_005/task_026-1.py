# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.

# 5
# 1
# 2
# 3
# 4
# 5
# 5 4 3 2 1

def print_numbers(n):
    number = int(input(f'число №{n}: '))
    if n > 1:
        print_numbers(n-1)
    print(number,end=" ")

n = int(input('n = '))
print_numbers(n)