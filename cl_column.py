from tkinter import *


class Create_column(Frame):
    # Конструктор этого класса поддерживает дополнительный параметр parent, с которым передается ссылка на главное окно
    # Она понадобится нам, чтобы вывести занесенное значение (имя колонки) в главном окне (Axello)
    def __init__(self, master, parent):
        super(Create_column, self).__init__(master)
        self.parent = parent  # Сохраним ссылку на главное окно в атрибуте
        self.grid()
        self.get_name()
        self.master.title("Создать колонку")
        self.master.geometry('+' + str(self.parent.start_x + 10) + '+150')
        self.master.resizable(False, False)
        self.focus_set()  # He забываем принудительно активизировать выведенное окно

    def get_name(self):
        self.cname = StringVar(value='Новая колонка')  # по умолчанию будет value = 'Новая колонка'

        lbl = Label(self, text='Введите название колонки\n(например, Новая колонка)')
        lbl.grid(row=0, column=0, columnspan=2)

        name_ent = Entry(self, width=30, textvariable=self.cname)
        name_ent.grid(row=1, column=0, columnspan=2, padx=[5, 5], pady=[5, 5])

        ready_btn = Button(self, text='Создать', command=self.ready)
        ready_btn.grid(row=2, column=0, sticky=W, padx=[5, 5], pady=[5, 5])

        cancel_btn = Button(self, text='Отмена', command=self.master.destroy)
        cancel_btn.grid(row=2, column=1, sticky=E, padx=[5, 5], pady=[5, 5])

    def ready(self):
        self.parent.col_name = self.cname.get()
        self.master.destroy()

        column = Column(self.parent.col_name, self.parent.start_x, self.parent.width_of_column)
        column.create_column_widgets()

        self.parent.start_x += int(self.parent.width_of_column * 7.5)
        self.parent.new_list_bttn.place(x=self.parent.start_x, y=110)


class Column():
    def __init__(self, column_name: str, start_x: int, width_of_column: int):
        self.name = column_name
        self.start_x = start_x
        self.width_of_column = width_of_column
        self.cards = []

    def create_column_widgets(self):
        self.column_back_lbl = Label(height=51, width=self.width_of_column)
        self.column_back_lbl.place(x=self.start_x, y=110)

        self.column_name_lbl = Label(text=self.name)
        self.column_name_lbl.place(x=self.start_x + 5, y=115)

        self.name_card_ent = Entry(width=25)
        self.name_card_ent.place(x=self.start_x + 5, y=135)

        self.add_name_card_bttn = Button(text='Добавить', bg='#B8D41D', fg='#515F0B')
        self.add_name_card_bttn.place(x=self.start_x + 165, y=132)

        self.delete_name_card_bttn = Button(text='Удалить', bg='#F08080', fg='#800000')
        self.delete_name_card_bttn.place(x=self.start_x + 170, y=850)

    def rename_column(self):
        self.name = input('Введите название столбца (например, Новый столбец)')
