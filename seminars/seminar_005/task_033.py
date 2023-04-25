# Задача №33. Общее обсуждение
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_grades(line):
    result = ''
    grades = str(line).split()
    min_grade = min(grades)
    max_grade = max(grades)

    for el in grades:
        if el == max_grade:
            el = min_grade
        result += el + ' '
    return result

line = input()
print(change_grades(line))
