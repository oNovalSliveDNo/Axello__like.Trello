from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Для входа введите логин, пароль").grid(row=0, column=0, sticky=W)
        Label(self, text="Логин:").grid(row=1, column=0, sticky=W)
        Label(self, text="Пароль:").grid(row=2, column=0, sticky=W)
        self.password_ent = Entry(self)
        self.password_ent.grid(row=2, column=1, sticky=W)
        self.login_ent = Entry(self)
        self.login_ent.grid(row=1, column=1, sticky=W)
        Button(self, text="ВХОД").grid(row=4, column=1, sticky=W)

root = Tk()
root.title("Пользовательский вход")
root.geometry("500x385")
app = Application(root)
root.mainloop()

