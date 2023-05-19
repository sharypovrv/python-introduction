arr = [1, 2, 3, 5, 8, 15, 23, 38]
result = list()

for el in arr:
    if el % 2 == 0:
        result.append([el, el * el])

print(result)