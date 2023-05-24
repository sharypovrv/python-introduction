menu = '''========================================
Меню:
0 - выход из меню
1 - добавление контакта
2 - вывод всех контактов
3 - поиск по фамилии
4 - удалить контакт по фамилии
5 - изменить номер по фамилии'''

def start():
    print('Здравствуйте!')

def end():
    print('Всего доброго!')

def readCommand():
    try:
        print(menu)
        command = int(input('Введите команду: '))
        if command < 0 or command > 5:
            print('Неправильная команда!')
        print('========================================')
        return command
    except ValueError:
        print('Неправильная команда!')

def printAddContact():
    print('Введите фамилию и номер через пробел: ')

def printAllContacts(allContacts):
    print('Список всех контактов:')
    if len(allContacts) == 0:
        print('Нет контактов.')
    else:
        for contact in allContacts:
            print('    ' + contact)

def inputSurname():
    return input('Введите фамилию: ')

def inputNumber():
    return input('Введите номер телефона: ')

def printRightContact(findContact):
    print('Результат поиска:')
    if findContact[0]:
        print(findContact[1])
    else:
        print('Нет такого контакта.')

def printDeleteContact(isSuccess):
    if isSuccess:
        print('Контакт удален.')
    else:
        print('Такого контакта нет.')

def printChangeBySurname(isSuccess):
    if isSuccess:
        print('Контакт изменен.')
    else:
        print('Такого контакта нет.')