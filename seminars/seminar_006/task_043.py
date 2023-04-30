# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3 
# Вывод:
# 2

def inputArray():
    return list(map(int, str(input()).split()))

def countCouples(inArr):
    count = 0
    for i in range(len(inArr) - 1):
        for j in range(i + 1, len(inArr)):
            if inArr[i] == inArr[j]:
                count += 1
    return count

arr = inputArray()
print(countCouples(arr))
