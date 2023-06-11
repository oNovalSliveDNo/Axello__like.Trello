from cl_tasktracker import *
from cl_board import Board


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
        self.btype = StringVar(value="Общественная")    # по умолчанию будет выбран элемент с value = 'Общественная'

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
        ready_btn.grid(row=3, column=2, sticky=W, padx=[5, 5], pady=[5, 5])

        cancel_btn = Button(self, text='Отмена', command=self.master.destroy)
        cancel_btn.grid(row=3, column=0,sticky=E, padx=[5, 5], pady=[5, 5])

    def ready(self):
        self.parent.board_name = self.bname.get()
        self.parent.board_type = self.btype.get()
        self.master.destroy()

        board = Board(users[-1], self.parent.board_name, self.parent.board_type, self.parent.start_x, self.parent.width_of_column)
        board.create_board_widgets()
