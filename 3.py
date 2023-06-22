class Rename_board(Frame):
    # Конструктор этого класса поддерживает дополнительный параметр parent, с которым передается ссылка на главное окно
    # Она понадобится нам, чтобы вывести занесенное значение (имя колонки) в главном окне (Axello)
    def __init__(self, master, parent):
        super(Rename_board, self).__init__(master)
        self.parent = parent  # Сохраним ссылку на главное окно в атрибуте
        self.master.title("Переименовать доску")
        self.master.geometry('+230+200')
        self.master.resizable(False, False)

        self.grid()
        self.get_name()

        self.focus_set()  # He забываем принудительно активизировать выведенное окно

    def get_name(self):
        # ==============================VARIABLES======================================

        self.nbname = StringVar(value='')

        # ==============================LABELS=========================================

        back_lbl = Label(self, bg='#9DB0FF', width=30, height=1)
        back_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        lbl = Label(self, text='Введите название доски', bg='#9DB0FF', fg='#03273F')
        lbl.grid(row=0, column=0, columnspan=2)

        # ==============================ENTRY WIDGETS==================================

        name_ent = Entry(self, width=30, textvariable=self.nbname)
        name_ent.grid(row=1, column=0, columnspan=2, padx=[5, 5], pady=[5, 5])

        # ==============================BUTTON WIDGETS=================================

        ready_btn = Button(self, text='Переименовать', command=self.ready, bg='#B8D41D', fg='#515F0B')
        ready_btn.grid(row=2, column=0, sticky=W, padx=[5, 5], pady=[5, 5])

        cancel_btn = Button(self, text='Отмена', command=self.master.destroy, bg='#F08080', fg='#800000')
        cancel_btn.grid(row=2, column=1, sticky=E, padx=[5, 5], pady=[5, 5])

    def ready(self):
        self.master.destroy()

        b_id = self.parent.board_id
        b_name = self.nbname.get()

        db.change_board_name(b_id, b_name)

        self.parent.open_board(self.parent.flag)


class Create_board(Frame):
    # Конструктор этого класса поддерживает дополнительный параметр parent, с которым передается ссылка на главное окно.
    # Она понадобится нам, чтобы вывести занесенное значение (имя доски) в главном окне (Axello)
    def __init__(self, master, parent):
        super(Create_board, self).__init__(master)
        self.parent = parent  # Сохраним ссылку на главное окно в атрибуте
        self.master.title("Создать доску")
        self.master.geometry('+230+100')
        self.master.resizable(False, False)

        self.grid()
        self.give_name_and_type()

        self.focus_set()  # He забываем принудительно активизировать выведенное окно

    def give_name_and_type(self):

        # ==============================VARIABLES======================================

        self.bname = StringVar(value='Новая доска')  # по умолчанию будет выбран элемент с value = 'Новая доска'
        self.btype = StringVar(value="Общественная")  # по умолчанию будет выбран элемент с value = 'Общественная'

        # ==============================LABELS=========================================

        back_lbl = Label(self, bg='#9DB0FF', width=21, height=6)
        back_lbl.grid(row=0, column=0, rowspan=2, sticky=W)

        lbl = Label(self, text='Введите название доски\n(например, Новая доска)', bg='#9DB0FF', fg='#03273F')
        lbl.grid(row=0, column=0)

        lbl = Label(self, text='Укажите тип доски', bg='#9DB0FF', fg='#03273F')
        lbl.grid(row=1, column=0, rowspan=2, padx=[5, 5], pady=[5, 5])

        # ==============================ENTRY WIDGETS==================================

        name_ent = Entry(self, width=30, textvariable=self.bname)
        name_ent.grid(row=0, column=1, columnspan=2, padx=[5, 5], pady=[5, 5])

        # ==============================BUTTON WIDGETS=================================

        ready_btn = Button(self, text='Создать', command=self.ready, bg='#B8D41D', fg='#515F0B')
        ready_btn.grid(row=3, column=0, sticky=W, padx=[5, 5], pady=[5, 5])

        cancel_btn = Button(self, text='Отмена', command=self.master.destroy, bg='#F08080', fg='#800000')
        cancel_btn.grid(row=3, column=2, sticky=E, padx=[5, 5], pady=[5, 5])

        # ==============================RADIO BUTTON WIDGETS===========================

        public_rbtn = Radiobutton(self, text="Частная", value="Частная", variable=self.btype)
        public_rbtn.grid(row=1, column=1, padx=[5, 5], pady=[5, 5])

        private_rbtn = Radiobutton(self, text="Общественная", value="Общественная", variable=self.btype)
        private_rbtn.grid(row=1, column=2, padx=[5, 5], pady=[5, 5])

    def ready(self):
        self.parent.board_name = self.bname.get()
        self.parent.board_type = self.btype.get()
        self.master.destroy()

        b_name = self.parent.board_name
        b_type = self.parent.board_type
        b_creator_id = db.user_objects[-1].user_id

        if b_type == 'Частная':
            db.insert_board(b_name, 'Частная', b_creator_id)
        else:
            db.insert_board(b_name, 'Общественная', b_creator_id)

        self.parent.create_menu_widgets()


class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_id = None
        self.owner_board_objects = list()
        self.party_board_objects = list()
        self.important_board_objects = list()
        self.public_board_objects = list()


class Board():
    def __init__(self, name: str, btype: str, important: bool):
        self.name = name
        self.type = btype
        self.important = important
        self.board_id = None
        self.columns = list()


class Column():
    def __init__(self, column_name: str):
        self.name = column_name
        self.column_id = None
        self.cards = list()


class Card():
    def __init__(self, name: str, sequence_number: int):
        self.name = name
        self.sequence_number = sequence_number
        self.card_id = None
