import view, controller
from datetime import date
from note import Note

working = True

view.start()
notes = controller.importListFromFile()
while (working):
    command = view.readCommand()
    match command:
        case 0:
            view.end()
            controller.exportListToFile()
            working = False
        case 1:
            allNote = controller.getAllNotes()
            view.printAllNotes(allNote)
        case 2:
            findTitle = view.inputTitle()
            if (controller.isContainsByTitle(findTitle)):
                findNote = controller.getNoteByTitle(findTitle)
                view.printNote(findNote)
            else:
                view.printSuccess(False)
        case 3:
            id = view.inputId()
            title = view.inputTitle()
            body = view.inputBody()
            controller.addNote(id, title, body, date.today())
        case 4:
            title = view.inputTitle()
            newBody = view.inputBody()
            view.printSuccess(controller.changeByTitle(title, newBody))
        case 5:
            deleteTitle = view.inputTitle()
            view.printSuccess(controller.deleteByTitle(deleteTitle))
            
            

