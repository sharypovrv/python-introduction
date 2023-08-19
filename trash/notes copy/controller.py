from note import Note
from datetime import date, datetime
import json

path = 'notes/notes.txt'

def getAllNotes():
    allNotes = list()
    try:
        data = open(path, 'r', encoding='utf-8')
        for line in data:
            allNotes.append(getNoteFromString(line))
        data.close()
    except FileNotFoundError:
        pass
    return allNotes

def getNoteByTitle(inputTitle):
    notes = getAllNotes()
    for item in notes:
        item: Note
        if item.title == inputTitle.lower():
            return item
    return Note()


def addNote(inputNote: Note):
    data = open(path, 'a', encoding='utf-8')
    data.write(inputNote.info() + '\n')
    data.close

    with open('notes/test.json', 'r', encoding='utf-8') as f:
        data_json = json.load(f)
        print(data_json)
    data_json["Notes"].append(inputNote.to_json())
    with open('notes/test.json', 'w') as f:
        json.dump(data_json, f, ensure_ascii=False, indent=3)

def deleteByTitle(inputTitle: str):
    if isContainsByTitle(inputTitle):
        data = open(path, 'w', encoding='utf-8')
        notes = getAllNotes()
        for item in notes:
            item: Note
            if item.title != inputTitle.lower():
                data.write(item.info() + '\n')
        data.close()
        return True
    return False

def changeByTitle(inputTitle, newBody):
    if isContainsByTitle(inputTitle):
        data = open(path, 'w', encoding='utf-8')
        notes = getAllNotes()
        for item in notes:
            item: Note
            if item.title != inputTitle.lower():
                item.body = newBody
                item.date = date.today()
            data.write(item.info() + '\n')
        data.close()
        return True
    return False

def getNoteFromString(line: str):
    arr = line.split(';')
    temp = datetime.strptime(arr[3][:-1], '%Y-%m-%d').date()
    return Note(arr[0], arr[1], arr[2], temp)

def isContainsByTitle(inputTitle):
    notes = getAllNotes()
    for item in notes:
        item: Note
        if item.title == inputTitle.lower():
            return True
    return False