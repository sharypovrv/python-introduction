# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии

# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм

# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход

import interface, dataFile

interface.start()

working = True

while working:
    command = interface.readCommand()
    match command:
        case 0:
            interface.end()
            working = False
        case 1:
            interface.printAddContact()
            dataFile.addContact(input())
        case 2:
            allContacts = dataFile.getAllContacts()
            interface.printAllContacts(allContacts)
        case 3:
            findSurname = interface.inputSurname()
            interface.printRightContact(dataFile.findBySurname(findSurname))
        case 4:
            deleteSurname = interface.inputSurname()
            interface.printDeleteContact(dataFile.deleteBySurname(deleteSurname))
        case 5:
            changeSurname = interface.inputSurname()
            newNumber = interface.inputNumber()
            interface.printChangeBySurname(dataFile.changeBySurname(changeSurname, newNumber))

            
