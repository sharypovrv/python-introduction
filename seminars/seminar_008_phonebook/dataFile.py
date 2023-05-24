path = 'seminars\seminar_008_phonebook\contacts.txt'

def getAllContacts():
    data = open(path, 'r', encoding='utf-8')
    allContacts = list()
    for contact in data:
        allContacts.append(contact[:-1])
    data.close()
    return allContacts

def addContact(line):
    data = open(path, 'a', encoding='utf-8')
    data.write(line + '\n')
    data.close

def findBySurname(inputSurname):
    isContains = False
    rightContact = str()

    for contact in getAllContacts():
        if contact.lower().split()[0] == inputSurname.lower():
            isContains = True
            rightContact = contact

    return (isContains, rightContact)

def deleteBySurname(inputSurname):
    isSuccess = False

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    f.close()

    for contact in lines:
        if contact.lower().split()[0] == inputSurname.lower():
            isSuccess = True
    
    if isSuccess:
        data = open(path, 'w', encoding='utf-8')
        for contact in lines:
            if contact.lower().split()[0] != inputSurname.lower():
                data.write(contact)
        data.close()

    return isSuccess

def changeBySurname(inputSurname, newNumber):
    isSuccess = False

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    f.close()

    for contact in lines:
        if contact.lower().split()[0] == inputSurname.lower():
            isSuccess = True
    
    if isSuccess:
        data = open(path, 'w', encoding='utf-8')
        for contact in lines:
            if contact.lower().split()[0] == inputSurname.lower():
                data.write(inputSurname + ' ' + newNumber + '\n')
            else:
                data.write(contact)
        data.close()

    return isSuccess
