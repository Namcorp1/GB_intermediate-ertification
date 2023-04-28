from tkinter import *
from tkinter import scrolledtext
import subprocess


def addNote():
    db = open("dbNotes.txt", "r+")
    nameNote = txtName.get()
    textNote = txtNote.get("1.0", "end")
    numNote = int(db.readlines()[0][0]) + 1
    note = f"{numNote};{nameNote};{textNote}\n"
    db.write(note)
    oldNum = db.read()
    newNum = oldNum.replace(f"{numNote - 1} - заметок",f"{numNote} - заметок")
    db.write(newNum)
    db.close()


addNoteWindow = Tk()
addNoteWindow.title('New note')
addNoteWindow.geometry('720x1280')
lblName = Label(addNoteWindow, text="Note name:")
lblName.grid(column=0, row=0)
txtName = Entry(addNoteWindow, width=51)
txtName.grid(column=1, row=0)
lblText = Label(addNoteWindow, text="Note text")
lblText.grid(column=0, row=1)
txtNote = scrolledtext.ScrolledText(addNoteWindow, width=64, height=30)
txtNote.grid(column=1, row=1)
btnSave = Button(addNoteWindow, text='Save', command=addNote)
btnSave.grid(column=0, row=2)
btnSaveAs = Button(addNoteWindow, text='Save as')
btnSaveAs.grid(column=0, row=3)
addNoteWindow.mainloop()
