path = 'seminars\seminar_008_phonebook\contacts.txt'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
f.close()

inputSurname = input()
newNumber = input()

data = open(path, 'w', encoding='utf-8')
for contact in lines:
    if contact.lower().split()[0] == inputSurname.lower():
        data.write(inputSurname + ' ' + newNumber + '\n')
    else:
        data.write(contact)
data.close()