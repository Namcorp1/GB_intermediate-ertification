from tkinter import *
import subprocess
def start():
    subprocess.run(["python", "mainWindow.py"])

def addNote():
    subprocess.run(["python", "addNoteWindow.py"])

mainWindow = Tk()
mainWindow.title('MyNotes')
mainWindow.geometry('720x1280')
btnNew = Button(mainWindow,text='New note',command=addNote)
btnNew.grid(column=1,row=0)
btnShow = Button(mainWindow,text='Show notes')
btnShow.grid(column=2,row=0)
btnExit = Button(mainWindow,text='Exit')
btnExit.grid(column=3,row=0)
mainWindow.mainloop()

