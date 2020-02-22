from tkinter import *

class BlockCode:
    def __init__(self, master):
        self.entry = Entry(master, width="20")
        self.button = Button(master, text="Forward")
        self.label = Label(master, width="20", bg="black", fg="white")
        self.entry.pack()
        self.button.pack()
        self.label.pack()

    def evalFunc(self, func):
        self.button['command'] = eval('self.' + func)

    def setTextLabel(self):
        s = self.entry.get()
        self.label['text'] = ''.join(s)

    def reverseTextLabel(self):
        s = self.entry.get()
        s = s[::-1]
        self.label['text'] = ''.join(s)


window = Tk()
block_one = BlockCode(window)
block_one.evalFunc('setTextLabel')
block_two = BlockCode(window)
block_two.evalFunc('reverseTextLabel')

window.mainloop()
