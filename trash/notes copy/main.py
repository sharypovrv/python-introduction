import view, controller, note
from datetime import date
from note import Note

working = True

view.start()

while (working):
    command = view.readCommand()
    match command:
        case 0:
            view.end()
            working = False
        case 1:
            allNote = controller.getAllNotes()
            view.printAllNotes(allNote)
        case 2:
            title = view.inputTitle()
            if (controller.isContainsByTitle(title)):
                findNote = controller.getNoteByTitle(title)
                # findNote: Note
                view.printNote(findNote)
            else:
                view.printSuccess(False)
        case 3:
            id = view.inputId()
            title = view.inputTitle()
            body = view.inputBody()
            newNote = note.Note(id, title, body, date.today())
            controller.addNote(newNote)
        case 4:
            title = view.inputTitle()
            newBody = view.inputBody()
            view.printSuccess(controller.changeByTitle(title, newBody))
        case 5:
            deleteTitle = view.inputTitle()
            view.printSuccess(controller.deleteByTitle(deleteTitle))
            
            

