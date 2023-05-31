from tkinter import *
from PIL import ImageTk, Image


class Back(Frame):
    def __init__(self, master):
        super(Back, self).__init__(master)
        self.grid()
        self.create_back_menu()

    def create_back_menu(self):
        self.back_lbl = Label(bg='#8FA0E8', width=214, height=3)
        self.back_lbl.grid(row=0, column=0, columnspan=11, sticky=NW)

        self.back_lbl = Label(bg='#9DB0FF', width=214, height=3)
        self.back_lbl.grid(row=1, column=0, columnspan=11, sticky=NW)

        self.back_lbl = Label(bg='#9DB0FF', width=7, height=55)
        self.back_lbl.grid(row=2, column=0, columnspan=11, sticky=NW)


class Menu(Frame):
    def __init__(self, master):
        super(Menu, self).__init__(master)
        self.grid()
        self.count = 0
        self.create_menu_widgets()
        self.create_scnd_menu_widgets()


    def create_menu_widgets(self):
        self.home_bttn = Button(text='Домой', height=2, bg='#03273F', fg='#B1D2E7')
        self.recent_bttn = Button(text='Недавние', height=2, bg='#B1D2E7', fg='#03273F')
        self.favourites_bttn = Button(text='В избранном', height=2, bg='#B1D2E7', fg='#03273F')
        self.new_board_bttn = Button(text='Создать доску', height=2, bg='#B8D41D', fg='#515F0B')

        self.search_bttn = Button(text='Поиск:', height=2, bg='#B1D2E7', fg='#03273F')
        self.search_ent = Entry(width=35, fg='#B1D2E7')
        self.notific_bttn = Button(text='Уведомления', height=2, bg='#B1D2E7', fg='#03273F')
        self.theme_bttn = Button(text='Тема', height=2, bg='#B1D2E7', fg='#03273F', command=self.add_to_count)
        self.profile_bttn = Button(text='Профиль', height=2, bg='#B1D2E7', fg='#03273F')
        self.exit_bttn = Button(text='Выход', height=2, bg='#03273F', fg='#B1D2E7', command=self.exit1)

        self.home_bttn.grid(row=0, column=0, padx=[2, 2], pady=[5, 5])
        self.recent_bttn.grid(row=0, column=1, padx=[2, 2], pady=[5, 5])
        self.favourites_bttn.grid(row=0, column=2, padx=[2, 2], pady=[5, 5])
        self.new_board_bttn.grid(row=0, column=3, padx=[2, 2], pady=[5, 5])
        self.search_bttn.grid(row=0, column=5, padx=[0, 2], pady=[5, 5])
        self.search_ent.grid(row=0, column=6, padx=[2, 2], pady=[5, 5])
        self.notific_bttn.grid(row=0, column=7, padx=[2, 2], pady=[5, 5])
        self.theme_bttn.grid(row=0, column=8, padx=[2, 2], pady=[5, 5])
        self.profile_bttn.grid(row=0, column=9, padx=[2, 2], pady=[5, 5])
        self.exit_bttn.grid(row=0, column=10, padx=[2, 5], pady=[5, 5])

    def create_scnd_menu_widgets(self):
        self.name_lbl = Label(text='Какое-то название доски', height=2, bg='#9DB0FF', fg='#03273F')
        self.delete_board_bttn = Button(text='Удалить', height=2, bg='#F08080', fg='#800000')
        self.rename_board_bttn = Button(text='Переименовать', height=2, bg='#B1D2E7', fg='#03273F')
        self.rename_board_ent = Entry(width=35, fg='#B1D2E7')
        self.add_to_favour_bttn = Checkbutton(text='Избранное', height=2, bg='#B1D2E7', fg='#03273F')
        self.new_list_bttn = Button(text='Создать список', height=2, bg='#B8D41D', fg='#515F0B')
        self.delete_list_bttn = Button(text='Удалить список', height=2, bg='#F08080', fg='#800000')
        self.left_bttn = Button(text='<=', height=2, bg='#F7DCBA', fg='#623803')
        self.right_bttn = Button(text='=>', height=2, bg='#F7DCBA', fg='#623803')
        self.invite_bttn = Button(text='Пригласить', height=2, bg='#B1D2E7', fg='#03273F')
        self.persons_bttn = Button(text='Участники', height=2, bg='#B1D2E7', fg='#03273F')

        self.name_lbl.grid(row=1, column=0, padx=[2, 2], pady=[5, 5])
        self.delete_board_bttn.grid(row=1, column=1, padx=[2, 2], pady=[5, 5])
        self.rename_board_bttn.grid(row=1, column=2, padx=[2, 2], pady=[5, 5])
        self.add_to_favour_bttn.grid(row=1, column=3, padx=[2, 2], pady=[5, 5])
        self.rename_board_ent.grid(row=1, column=4, padx=[2, 2], pady=[5, 5])
        self.new_list_bttn.grid(row=1, column=5, padx=[2, 2], pady=[5, 5])
        self.delete_list_bttn.grid(row=1, column=6, padx=[2, 2], pady=[5, 5])
        self.left_bttn.grid(row=1, column=7, padx=[2, 2], pady=[5, 5])
        self.right_bttn.grid(row=1, column=8, padx=[2, 2], pady=[5, 5])
        self.invite_bttn.grid(row=1, column=9, padx=[2, 2], pady=[5, 5])
        self.persons_bttn.grid(row=1, column=10, padx=[2, 2], pady=[5, 5])

    def add_to_count(self):
        self.count += 1
        if (self.count % 2) == 0:
            self.back_lbl = Label(bg='#8FA0E8', width=214, height=3)
            self.back_lbl.grid(row=0, column=0, columnspan=11, sticky=NW)

            self.back_lbl = Label(bg='#9DB0FF', width=214, height=3)
            self.back_lbl.grid(row=1, column=0, columnspan=11, sticky=NW)

            self.back_lbl = Label(bg='#9DB0FF', width=7, height=55)
            self.back_lbl.grid(row=2, column=0, columnspan=11, sticky=NW)
            self.create_menu_widgets()
            self.create_scnd_menu_widgets()

        if (self.count % 2) == 1:
            self.back_lbl = Label(bg='#191970', width=214, height=3)
            self.back_lbl.grid(row=0, column=0, columnspan=11, sticky=NW)

            self.back_lbl = Label(bg='#0000CD', width=214, height=3)
            self.back_lbl.grid(row=1, column=0, columnspan=11, sticky=NW)

            self.back_lbl = Label(bg='#0000CD', width=7, height=55)
            self.back_lbl.grid(row=2, column=0, columnspan=11, sticky=NW)
            self.create_menu_widgets()
            self.create_scnd_menu_widgets()

    def exit1(self):
        root.destroy()


class Lists(Frame):
    def __init__(self, master, count_of_lists):
        super(Application, self).__init__(master)
        self.grid()
        self.create_list()

if __name__ == '__main__':
    # создание базового окна
    root = Tk()
    root.title('Axello')
    root.geometry('1500x900+10+10')
    root.resizable(False, False)
    root.config(bg='#E0E0E0')

    # создание рамки для размещения элементов
    app = Back(root)
    app = Menu(root)


    # старт событийного цикла
    root.mainloop()