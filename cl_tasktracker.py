from tkinter import *
from database import *
from cl_user import *
from cl_board import *
from cl_column import *
from cl_card import *


class TaskTracker(Frame):
    def __init__(self, master):
        super(TaskTracker, self).__init__(master)
        self.start_x = 5
        self.width_of_column = 32
        self.grid()

        self.count_for_theme = 0
        if self.count_for_theme == 10:
            self.count_for_theme = 0

        self.back_lbl = Label(bg='#8FA0E8', width=214, height=3)
        self.home_bttn = Button(text='Домой', height=2, bg='#03273F', fg='#B1D2E7')
        self.recent_bttn = Button(text='Недавние', height=2, bg='#B1D2E7', fg='#03273F')
        self.favourites_bttn = Button(text='В избранном', height=2, bg='#B1D2E7', fg='#03273F')
        self.new_board_bttn = Button(text='Создать доску', height=2, bg='#B8D41D', fg='#515F0B', command=self.create_board)
        self.search_bttn = Button(text='Поиск:', height=2, bg='#B1D2E7', fg='#03273F')
        self.search_ent = Entry(width=35, fg='#B1D2E7')
        self.notific_bttn = Button(text='Уведомления', height=2, bg='#B1D2E7', fg='#03273F')
        self.theme_bttn = Button(text='Тема', height=2, bg='#B1D2E7', fg='#03273F')
        self.profile_bttn = Button(text='Профиль', height=2, bg='#B1D2E7', fg='#03273F')
        self.exit_bttn = Button(text='Выход', height=2, bg='#03273F', fg='#B1D2E7', command=self.quit)

        self.create_menu_widgets()

    def create_menu_widgets(self):
        self.back_lbl.grid(row=0, column=0, columnspan=11, sticky=NW)
        self.home_bttn.place(x=5, y=5)
        self.recent_bttn.place(x=60, y=5)
        self.favourites_bttn.place(x=130, y=5)
        self.new_board_bttn.place(x=220, y=5)
        self.search_bttn.place(x=970, y=5)
        self.search_ent.place(x=1020, y=15)
        self.notific_bttn.place(x=1240, y=5)
        self.theme_bttn.place(x=1335, y=5)
        self.profile_bttn.place(x=1380, y=5)
        self.exit_bttn.place(x=1450, y=5)

    def create_board(self):
        def dismiss(window):
            window.grab_release()
            window.destroy()

        def new_window():
            window_assign_name = Toplevel()
            window_assign_name.title("Введите название доски (например, Новая доска)")
            window_assign_name.geometry("250x100+" + str(self.start_x) + "+150")
            window_assign_name.resizable(False, False)
            window_assign_name.protocol("WM_DELETE_WINDOW",
                                        lambda: dismiss(window_assign_name))  # перехватываем нажатие на крестик

            write_board_name = Entry(window_assign_name, width=40)
            write_board_name.pack(anchor='nw', pady=[10, 10])

            board_name = write_board_name.get()

            get_name = Button(window_assign_name, text='Готово', command=lambda: dismiss(window_assign_name))
            get_name.pack(anchor='center')
            window_assign_name.grab_set()  # захватываем пользовательский ввод
            return board_name

        board_name = new_window()
        self.board = Board('456789hgf', board_name, 'Общественная', self.start_x, self.width_of_column)
        self.board.create_board_widgets()

    def create_card(self):
        pass
