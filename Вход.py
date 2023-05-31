from tkinter import *
import tkinter.messagebox as mb
from PIL import ImageTk, Image

class Back(Frame):
    def __init__(self, master):
        super(Back, self).__init__(master)
        self.grid()
        self.create_back_menu()


    def create_back_menu(self):
        self.back_lbl = Label(bg='#8FA0E8',width=214, height=3)
        self.back_lbl.grid(row=0, column=0, columnspan=10, sticky=NW)

        self.back_lbl = Label(bg='#9DB0FF', width=214, height=3)
        self.back_lbl.grid(row=1, column=0, columnspan=10, sticky=NW)


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.authorization_lbl = Label(text='АВТОРИЗАЦИЯ',width=14, height=2, bg='#9DB0FF', fg='#03273F')
        self.logpas_lbl = Label(text="Для входа введите логин, пароль", width=28, height=2, bg='#9DB0FF', fg='#03273F')
        self.log_lbl = Label(text="Логин:", width=14, height=2, bg='#9DB0FF', fg='#03273F')
        self.pas_lbl = Label(text="Пароль:", width=14, height=2, bg='#9DB0FF', fg='#03273F')
        self.password_ent = Entry(width=20,fg='#000000', show='*')
        self.login_ent = Entry(width=20, fg='#000000')
        self.entry_bttn = Button(text="ВХОД", height=2, bg = '#B1D2E7', fg='#03273F', command=self.check_log_pas)
        self.error_lbl = Label(bg='#E0E0E0', fg='#FF0000')

        self.error_lbl.grid(row=9,column=0)
        self.authorization_lbl.grid(row=0, column=0)
        self.logpas_lbl.grid(row=1, column=0)
        self.log_lbl.grid(row=4, column=0, sticky=W)
        self.pas_lbl.grid(row=6, column=0, sticky=W)
        self.password_ent.grid(row=6, column=0)
        self.login_ent.grid(row=4, column=0)
        self.entry_bttn.grid(row=7, column=0)

    def check_log_pas(self):
        if self.login_ent.get() == '' or self.password_ent.get() == '':
            self.error_lbl.config(text='Вы не ввели логин или пароль!')
        elif len(self.login_ent.get()) < 6 or len(self.login_ent.get()) > 20\
                or len(self.password_ent.get()) < 6 or len(self.password_ent.get()) > 20:
            self.error_lbl.config(text='Вы неправильно ввели логин или пароль')
        else:
            root.destroy()
            window = Tk()
            window.title('AXELLO ')
            window.geometry('1500x900+10+10')


if __name__ == '__main__':

    root = Tk()
    root.title('Вход')
    root.geometry('325x250+200+200')
    root.resizable(False, False)

    app = Back(root)
    app = Application(root)
    root.config(bg='#E0E0E0')

    root.mainloop()
