from cl_tasktracker import *


class Authorization(Frame):
    def __init__(self, master):
        super(Authorization, self).__init__(master)

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.back_lbl = Label(bg='#8FA0E8', width=38, height=4)
        self.back_lbl.grid(row=0, column=0, columnspan=3)

        self.back_lbl = Label(bg='#9DB0FF', width=14, height=6)
        self.back_lbl.grid(row=1, column=0, rowspan=2)

        self.authorization_lbl = Label(text='АВТОРИЗАЦИЯ', font='15', width=14, height=2, bg='#9DB0FF', fg='#03273F')
        self.authorization_lbl.grid(row=0, column=0, columnspan=3)

        self.log_lbl = Label(text="Логин:", width=11, height=2, bg='#9DB0FF', fg='#03273F')
        self.log_lbl.grid(row=1, column=0)

        self.pas_lbl = Label(text="Пароль:", width=11, height=2, bg='#9DB0FF', fg='#03273F')
        self.pas_lbl.grid(row=2, column=0)

        self.login_ent = Entry(width=25, fg='#000000')
        self.login_ent.grid(row=1, column=1)

        self.password_ent = Entry(width=25, fg='#000000', show='*')
        self.password_ent.grid(row=2, column=1)

        self.entry_bttn = Button(text="ВХОД", font='15', width=15, height=1, bg='#B1D2E7', fg='#03273F',
                                 command=self.check_log_pas)
        self.entry_bttn.grid(row=3, column=0, columnspan=3)

        self.error_lbl = Label(bg='#E0E0E0', fg='#FF0000')
        self.error_lbl.grid(row=4, column=0, columnspan=3)

    def check_log_pas(self):
        if (self.login_ent.get() == '') or (self.password_ent.get() == ''):
            self.error_lbl.config(text='Вы не ввели логин или пароль!')

        elif (len(self.login_ent.get()) < 4):
            self.error_lbl.config(text='Логин должен состоять хотя бы из 4 символов')

        elif (len(self.password_ent.get()) < 6):
            self.error_lbl.config(text='Пароль должен состоять хотя бы из 6 символов')

        elif (len(self.login_ent.get()) > 20):
            self.error_lbl.config(text='Логин не должен превышать 20 символов')

        elif (len(self.password_ent.get()) > 20):
            self.error_lbl.config(text='Пароль не должен превышать 20 символов')

        else:
            user = (self.login_ent.get(), self.password_ent.get())
            users.append(tuple(user))
            window.destroy()

            # создание базового окна
            root = Tk()
            root.title('Axello')
            root.geometry('1500x900+10+10')
            root.resizable(False, False)
            root.config(bg='#E0E0E0')

            # создание рамки для размещения элементов
            app = TaskTracker(master=root)

            # старт событийного цикла
            root.mainloop()


if __name__ == '__main__':
    # создание окна авторизации
    window = Tk()
    window.title('Вход')
    window.geometry('272x230+600+300')
    window.resizable(False, False)
    window.config(bg='#E0E0E0')

    # создание рамки для размещения элементов
    aut = Authorization(master=window)

    # старт событийного цикла
    window.mainloop()
