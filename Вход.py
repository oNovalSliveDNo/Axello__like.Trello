from tkinter import *
from PIL import ImageTk, Image

class Back(Frame):
    def __init__(self, master):
        super(Back, self).__init__(master)
        self.grid()
        self.create_back_menu()


    def create_back_menu(self):
        self.back_lbl = Label(bg='#8FA0E8',width=214, height=3)
        self.back_lbl.grid(row=0, column=0, columnspan=11, sticky=NW)

        self.back_lbl = Label(bg='#9DB0FF', width=214, height=3)
        self.back_lbl.grid(row=1, column=0, columnspan=11, sticky=NW)


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.authorization_lbl = Label(text='АВТОРИЗАЦИЯ',width=28, height=2, bg='#9DB0FF', fg='#03273F')
        self.logpas_lbl = Label(text="Для входа введите логин, пароль", width=28, height=2, bg='#9DB0FF', fg='#03273F')
        self.log_lbl = Label(text="Логин:", width=28, height=2, bg='#9DB0FF', fg='#03273F')
        self.pas_lbl = Label(text="Пароль:", width=28, height=2, bg='#9DB0FF', fg='#03273F')
        self.password_ent = Entry(width=30,fg='#B1D2E7')
        self.login_ent = Entry(width=30, fg='#B1D2E7')
        self.entry_bttn = Button(text="ВХОД", height=2, bg = '#B1D2E7', fg='#03273F')

        self.authorization_lbl.grid(row=0, column=4, columnspan=3, padx=[2, 2], pady=[5, 5])
        self.logpas_lbl.grid(row=1, column=4, columnspan=3, padx=[2, 2], pady=[5, 5])
        self.log_lbl.grid(row=2, column=3, columnspan=3, padx=[2, 2], pady=[5, 5])
        self.pas_lbl.grid(row=3, column=3, columnspan=3, padx=[2, 2], pady=[5, 5])
        self.password_ent.grid(row=3, column=5, columnspan=3, padx=[2, 2], pady=[5, 5])
        self.login_ent.grid(row=2, column=5, columnspan=3, padx=[2, 2], pady=[5, 5])
        self.entry_bttn.grid(row=4, column=6, padx=[2, 2], pady=[5, 5])

if __name__ == '__main__':

    root = Tk()
    root.title('Axello')
    root.geometry('1500x900+10+10')
    root.resizable(False, False)

    app = Back(root)
    app = Application(root)
    root.config(bg='#E0E0E0')

    root.mainloop()
