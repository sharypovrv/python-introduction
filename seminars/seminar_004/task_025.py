# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# line = str(input('Введите слово: '))
line = 'a a a b c a a d c d d'
list_insert = line.split()
list_result = list()
count = 1

for i in range(len(list_insert)):
    for j in range(i):
        if list_insert[i] == list_insert[j]:
            count += 1
    list_result.append(f'{list_insert[i]}_{count}') # можно print(f'{list_insert[i]}_{count}')
    count = 1
print(*list_insert)
print(*list_result)

# Решение из семинара
# dict1 = dict()

# symbols = input("Введите буквы: ")

# for syn in symbols:
#     if syn in dict1:
#         dict1[syn] +=1
#     else:
#         dict1[syn] = 0

#     if dict1[syn] == 0:
#         print(syn)
#     else:
#         print(f"{syn}_{dict1[syn]}")