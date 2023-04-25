class View(object):
    def showMenu(self):
        print("Выберите действие:")
        menu = ["1. Создать заметку","2. Просмотр списка заметок","3. Выход"]
        for i in menu:
            print(i)

    def showNotes(self,notes):
        number = 1
        print("Список заметок:")
        for i in notes:
            print(str(number) + ". " + i)
            number += 1

    def showFullNote(self,numNote,fullNotes):
        print(fullNotes[numNote - 1])