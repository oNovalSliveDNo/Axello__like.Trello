from cl_tasktracker import *
from database import *
from cl_column import *


class Create_board(Frame):
    # Конструктор этого класса поддерживает дополнительный параметр parent, с которым передается ссылка на главное окно
    # Она понадобится нам, чтобы вывести занесенное значение (имя доски) в главном окне (Axello)
    def __init__(self, master, parent):
        super(Create_board, self).__init__(master)
        self.parent = parent  # Сохраним ссылку на главное окно в атрибуте
        self.grid()
        self.give_name_and_type()
        self.master.title("Создать доску")
        self.master.geometry('+230+100')
        self.master.resizable(False, False)
        self.focus_set()  # He забываем принудительно активизировать выведенное окно

    def give_name_and_type(self):
        self.bname = StringVar(value='Новая доска')  # по умолчанию будет выбран элемент с value = 'Новая доска'
        self.btype = StringVar(value="Общественная")  # по умолчанию будет выбран элемент с value = 'Общественная'

        lbl = Label(self, text='Введите название доски\n(например, Новая доска)')
        lbl.grid(row=0, column=0)

        name_ent = Entry(self, width=30, textvariable=self.bname)
        name_ent.grid(row=0, column=1, columnspan=2, padx=[5, 5], pady=[5, 5])

        lbl = Label(self, text='Укажите тип доски')
        lbl.grid(row=1, column=0, rowspan=2, padx=[5, 5], pady=[5, 5])

        public_rbtn = Radiobutton(self, text="Частная", value="Частная", variable=self.btype)
        public_rbtn.grid(row=1, column=1, padx=[5, 5], pady=[5, 5])

        private_rbtn = Radiobutton(self, text="Общественная", value="Общественная", variable=self.btype)
        private_rbtn.grid(row=1, column=2, padx=[5, 5], pady=[5, 5])

        ready_btn = Button(self, text='Создать', command=self.ready)
        ready_btn.grid(row=3, column=0, sticky=W, padx=[5, 5], pady=[5, 5])

        cancel_btn = Button(self, text='Отмена', command=self.master.destroy)
        cancel_btn.grid(row=3, column=2, sticky=E, padx=[5, 5], pady=[5, 5])

    def ready(self):
        self.parent.board_name = self.bname.get()
        self.parent.board_type = self.btype.get()
        self.master.destroy()

        board = Board(users[-1], self.parent.board_name, self.parent.board_type, self.parent.start_x,
                      self.parent.width_of_column)
        board.create_board_widgets()


class Rename_board(Frame):
    # Конструктор этого класса поддерживает дополнительный параметр parent, с которым передается ссылка на главное окно
    # Она понадобится нам, чтобы вывести занесенное значение (имя колонки) в главном окне (Axello)
    def __init__(self, master, parent):
        super(Rename_board, self).__init__(master)
        self.parent = parent  # Сохраним ссылку на главное окно в атрибуте
        self.grid()
        self.get_name()
        self.master.title("Переименовать доску")
        self.master.geometry('+230+200')
        self.master.resizable(False, False)
        self.focus_set()  # He забываем принудительно активизировать выведенное окно

    def get_name(self):
        self.nbname = StringVar(value=self.parent.name)  # по умолчанию будет value = <Текущее название доски>

        lbl = Label(self, text='Введите название доски')
        lbl.grid(row=0, column=0, columnspan=2)

        name_ent = Entry(self, width=30, textvariable=self.nbname)
        name_ent.grid(row=1, column=0, columnspan=2, padx=[5, 5], pady=[5, 5])

        ready_btn = Button(self, text='Переименовать', command=self.ready)
        ready_btn.grid(row=2, column=0, sticky=W, padx=[5, 5], pady=[5, 5])

        cancel_btn = Button(self, text='Отмена', command=self.master.destroy)
        cancel_btn.grid(row=2, column=1, sticky=E, padx=[5, 5], pady=[5, 5])

    def ready(self):
        self.parent.name = self.nbname.get()
        self.master.destroy()
        self.parent.create_board_widgets()


class Board():
    def __init__(self, owner: str, name: str, btype: str, start_x: int, width_of_column: int):
        self.name = name
        self.type = btype
        self.start_x = start_x
        self.width_of_column = width_of_column
        self.owner = owner
        self.columns = []

    def create_board_widgets(self):
        self.new_list_bttn = Button(text='  +  Добавить список', height=2, bg='#B8D41D', fg='#515F0B',
                                    command=self.create_column)
        self.new_list_bttn.place(x=self.start_x, y=110)

        self.back_lbl = Label(text=' ', bg='#9DB0FF', width=214, height=3)
        self.back_lbl.grid(row=1, column=0, columnspan=11, sticky=NW)

        self.name_lbl = Label(text=self.name, height=2, font='11', bg='#9DB0FF', fg='#03273F')
        self.name_lbl.place(y=50)

        self.delete_board_bttn = Button(text='Удалить доску', height=2, bg='#F08080', fg='#800000')
        self.delete_board_bttn.place(x=220, y=55)

        self.rename_board_bttn = Button(text='Переименовать', height=2, bg='#B1D2E7', fg='#03273F',
                                        command=self.rename_board)
        self.rename_board_bttn.place(x=315, y=55)

        self.add_to_favour_bttn = Checkbutton(text='Избранное', height=2, bg='#B1D2E7', fg='#03273F')
        self.add_to_favour_bttn.place(x=420, y=55)

        self.invite_bttn = Button(text='Пригласить', height=2, bg='#B1D2E7', fg='#03273F')
        self.invite_bttn.place(x=1345, y=55)

        self.persons_bttn = Button(text='Участники', height=2, bg='#B1D2E7', fg='#03273F')
        self.persons_bttn.place(x=1427, y=55)

    def rename_board(self):
        Rename_board(master=Toplevel(), parent=self)

    def create_column(self):
        self.new_list_bttn.forget()
        self.col_name = ''

        # Выводим вторичное окно, не забыв указать в параметре parent конструктора ссыпку на главное окно
        Create_column(master=Toplevel(), parent=self)
