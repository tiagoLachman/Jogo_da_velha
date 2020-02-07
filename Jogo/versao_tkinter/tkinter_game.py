from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Frame.__init__(self, master)
        self.msg = Label(self, text="Hello World")
        self.msg.pack()
        self.bye = Button(self, text="Bye", command=self.quit)
        self.bye.pack()
        self.pack()


if __name__ == '__main__':
    app = App()
    app.master.title("Exemplo")
    app.master.geometry("200x200+2000+10")
    mainloop()
