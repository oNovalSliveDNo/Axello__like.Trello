from tkinter import *
from PIL import ImageTk, Image

class Back(Frame):
    def __init__(self, master):
        super(Back, self).__init__(master)
        self.grid()
        self.create_back_menu()
        self.create_back_board()

    def create_back_menu(self):
        self.back_lbl = Label(bg='#8FA0E8',width=214, height=3)
        self.back_lbl.grid(row=0, column=0, columnspan=11, sticky=NW)

        self.back_lbl = Label(bg='#9DB0FF', width=214, height=3)
        self.back_lbl.grid(row=1, column=0, columnspan=11, sticky=NW)

        self.back_lbl = Label(bg='#9DB0FF', width=7, height=55)
        self.back_lbl.grid(row=2, column=0, columnspan=11, sticky=NW)

    def create_back_board(self):
        self.back_lbl = Label(bg='#FFFFFF', width=28, height=5)
        self.back_lbl.grid(row=2, column=1, columnspan=3, sticky=NW, padx = 5, pady=7)

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_menu_widgets()
        self.create_scnd_menu_widgets()
        self.create_board_widgets()

    def create_menu_widgets(self):
        self.menu_bttn = Button(text='Меню', width=6, height=2, bg = '#F7DCBA', fg='#623803')
        self.home_bttn = Button(text='Домой', width=6, height=2,bg = '#03273F', fg='#B1D2E7')
        self.recent_bttn = Button(text='Недавние', height=2,bg = '#B1D2E7', fg='#03273F')
        self.favourites_bttn = Button(text='В избранном', height=2,bg = '#B1D2E7', fg='#03273F')
        self.new_board_bttn = Button(text='Создать', width=10, height=2,bg = '#B8D41D', fg='#515F0B')
        self.search_bttn = Button(text='Поиск:', width=6, height=2,bg = '#B1D2E7', fg='#03273F')
        self.search_ent = Entry(width=30,fg='#B1D2E7')
        self.notific_bttn = Button(text='Уведомления', height=2,bg = '#B1D2E7', fg='#03273F')
        self.theme_bttn = Button(text='Тема', width=6, height=2,bg = '#B1D2E7', fg='#03273F')
        self.profile_bttn = Button(text='Профиль', height=2,bg = '#B1D2E7', fg='#03273F')
        self.exit_bttn = Button(text='Выход', width=6, height=2,bg = '#03273F', fg='#B1D2E7')

        self.menu_bttn.grid(row=0, column=0, padx=[2, 2], pady=[5, 5])
        self.home_bttn.grid(row=0, column=1, padx=[2, 2], pady=[5, 5])
        self.recent_bttn.grid(row=0, column=2, padx=[2, 2], pady=[5, 5])
        self.favourites_bttn.grid(row=0, column=3, padx=[2, 2], pady=[5, 5])
        self.new_board_bttn.grid(row=0, column=4, padx=[2, 2], pady=[5, 5])
        self.search_bttn.grid(row=0, column=5, padx=[600, 2], pady=[5, 5])
        self.search_ent.grid(row=0, column=6, padx=[2, 2], pady=[5, 5])
        self.notific_bttn.grid(row=0, column=7, padx=[2, 2], pady=[5, 5])
        self.theme_bttn.grid(row=0, column=8, padx=[2, 2], pady=[5, 5])
        self.profile_bttn.grid(row=0, column=9, padx=[2, 2], pady=[5, 5])
        self.exit_bttn.grid(row=0, column=10, padx=[2, 2], pady=[5, 5])

    def create_scnd_menu_widgets(self):
        self.name_lbl = Label(text='Какое-то название доски', width=28, height=2, bg='#9DB0FF', fg='#03273F')
        self.add_to_favour_bttn = Checkbutton(text='Избранное', width=10, height=2,bg = '#B1D2E7', fg='#03273F')
        self.invite_bttn = Button(text='Пригласить участника', height=2,bg = '#B1D2E7', fg='#03273F')
        self.count_pers_lbl = Label(text='Участников: 1', bg='#9DB0FF', fg='#03273F')
        self.persons_bttn = Button(text='Участники', height=2,bg = '#B1D2E7', fg='#03273F')
        self.menu_bttn = Button(text='Меню', width=6, height=2,bg = '#F7DCBA', fg='#623803')

        self.name_lbl.grid(row=1, column=1, columnspan=3, padx=[2, 2], pady=[5, 5])
        self.add_to_favour_bttn.grid(row=1, column=4, padx=[2, 2], pady=[5, 5])
        self.invite_bttn.grid(row=1, column=8, columnspan=2, padx=[2, 2], pady=[5, 5])
        self.count_pers_lbl.grid(row=1, column=6, padx=[2, 2], pady=[5, 5], sticky=E)
        self.persons_bttn.grid(row=1, column=7, padx=[2, 2], pady=[5, 5])
        self.menu_bttn.grid(row=1, column=10, padx=[2, 2], pady=[5, 5])

    def create_board_widgets(self):
        self.list_name_ent = Entry(width=32, fg='#000000')
        self.new_list_bttn = Button(text = 'Создать', width=7, height=2)
        self.bttn = Button(text = '123', width=6, height=2, bg='#000000')

        self.list_name_ent.grid(row=2, column=1, columnspan=3, sticky=NW, padx=[8, 0], pady=[10, 0])
        self.new_list_bttn.grid(row = 2, column=1, sticky=NW)