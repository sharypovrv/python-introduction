from note import Note

menu = '''========================================
Меню:
0 - выход из программы
1 - вывести список всех заметок
2 - вывести одну заметку
3 - добавление новой заметки
4 - редактировать заметку
5 - удалить заметку'''

def start():
    print('Программа запущена...')

def end():
    print('Программа завершена...')

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

def inputId():
    return input('Введите ID: ')

def inputTitle():
    return input('Введите заголовок заметки: ')

def inputBody():
    return input('Введите тело заметки: ')

def printAllNotes(allNotes):
    print('Список всех заметок:')
    if len(allNotes) == 0:
        print('Нет заметок.')
    else:
        for item in allNotes:
            print(item)

def printNote(inputNote: Note):
    print(inputNote)

def printSuccess(isSuccess: bool):
    if isSuccess:
        print("Успешно!")
    else:
        print("Операция не выполнена!")