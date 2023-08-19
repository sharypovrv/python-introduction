from note import Note
from datetime import date
import json

path = 'notes/notes.json'
notes = list()

def importListFromFile():
    l = list()
    with open(path, 'r', encoding='utf-8') as f:
        l = json.load(f)
    for item in l:
        notes.append(Note().from_dict(item))

def exportListToFile():
    to_json = list()
    for item in notes:
        item: Note
        to_json.append(item.to_dict())
    with open(path, 'w') as f:
        json.dump(to_json, f, ensure_ascii=False, indent=2)

def getAllNotes():
    return notes

def getNoteByTitle(inputTitle) -> Note:
    result = Note()
    for item in notes:
        item: Note
        if item.title == inputTitle:
            result = item
    return result

def addNote(id, title, body, date: date):
    notes.append(Note(id, title, body, date))

def deleteByTitle(inputTitle: str):
    if isContainsByTitle(inputTitle):
        for item in notes:
            item: Note
            if item.title == inputTitle:
                notes.remove(item)
        return True
    return False

def changeByTitle(inputTitle, newBody):
    if isContainsByTitle(inputTitle):
        for item in notes:
            item: Note
            if item.title == inputTitle:
                item.body = newBody
                item.date = date.today()
        return True
    return False

def isContainsByTitle(inputTitle: str):
    for item in notes:
        item: Note
        if item.title == inputTitle:
            return True
    return False