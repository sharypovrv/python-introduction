# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12, 5643]

list_1 = [12,'sadf', 5643, 'asd']
print(list_1)
list_2 = list(filter(lambda x: type(x) == int, list_1))
print(list_2)
list_3 = list(filter(lambda x: type(x) == str, list_1))
print(list_3)
