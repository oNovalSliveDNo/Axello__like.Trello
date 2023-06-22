from tkinter import *


class Rename_card(Frame):
    # Конструктор этого класса поддерживает дополнительный параметр parent, с которым передается ссылка на главное окно
    # Она понадобится нам, чтобы вывести занесенное значение (имя колонки) в главном окне (Axello)
    def __init__(self, master, parent):
        super(Rename_card, self).__init__(master)
        self.parent = parent  # Сохраним ссылку на главное окно в атрибуте
        self.master.title("Переименовать доску")
        self.master.geometry('+230+200')
        self.master.resizable(False, False)

        self.grid()
        self.get_name()

        self.focus_set()  # He забываем принудительно активизировать выведенное окно

    def get_name(self):
        # ==============================VARIABLES======================================

        self.nсname = StringVar(value='')

        # ==============================LABELS=========================================

        back_lbl = Label(self, bg='#9DB0FF', width=30, height=1)
        back_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        lbl = Label(self, text='Введите название карточки', bg='#9DB0FF', fg='#03273F')
        lbl.grid(row=0, column=0, columnspan=2)

        # ==============================ENTRY WIDGETS==================================

        name_ent = Entry(self, width=30, textvariable=self.nсname)
        name_ent.grid(row=1, column=0, columnspan=2, padx=[5, 5], pady=[5, 5])

        # ==============================BUTTON WIDGETS=================================

        ready_btn = Button(self, text='Переименовать', command=self.ready, bg='#B8D41D', fg='#515F0B')
        ready_btn.grid(row=2, column=0, sticky=W, padx=[5, 5], pady=[5, 5])

        cancel_btn = Button(self, text='Отмена', command=self.master.destroy, bg='#F08080', fg='#800000')
        cancel_btn.grid(row=2, column=1, sticky=E, padx=[5, 5], pady=[5, 5])

    def ready(self):
        self.master.destroy()

        c_id = self.parent.card_id
        c_name = self.nсname.get()

        db.change_card_name(c_id, c_name)

        self.parent.open_board(self.parent.flag)


class Rename_column(Frame):
    # Конструктор этого класса поддерживает дополнительный параметр parent, с которым передается ссылка на главное окно
    # Она понадобится нам, чтобы вывести занесенное значение (имя колонки) в главном окне (Axello)
    def __init__(self, master, parent):
        super(Rename_column, self).__init__(master)
        self.parent = parent  # Сохраним ссылку на главное окно в атрибуте
        self.master.title("Переименовать доску")
        self.master.geometry('+230+200')
        self.master.resizable(False, False)

        self.grid()
        self.get_name()

        self.focus_set()  # He забываем принудительно активизировать выведенное окно

    def get_name(self):
        # ==============================VARIABLES======================================

        self.nсname = StringVar(value='')

        # ==============================LABELS=========================================

        back_lbl = Label(self, bg='#9DB0FF', width=30, height=1)
        back_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        lbl = Label(self, text='Введите название колонки', bg='#9DB0FF', fg='#03273F')
        lbl.grid(row=0, column=0, columnspan=2)

        # ==============================ENTRY WIDGETS==================================

        name_ent = Entry(self, width=30, textvariable=self.nсname)
        name_ent.grid(row=1, column=0, columnspan=2, padx=[5, 5], pady=[5, 5])

        # ==============================BUTTON WIDGETS=================================

        ready_btn = Button(self, text='Переименовать', command=self.ready, bg='#B8D41D', fg='#515F0B')
        ready_btn.grid(row=2, column=0, sticky=W, padx=[5, 5], pady=[5, 5])

        cancel_btn = Button(self, text='Отмена', command=self.master.destroy, bg='#F08080', fg='#800000')
        cancel_btn.grid(row=2, column=1, sticky=E, padx=[5, 5], pady=[5, 5])

    def ready(self):
        self.master.destroy()

        c_id = self.parent.column_id
        c_name = self.nсname.get()

        db.change_column_name(c_id, c_name)

        self.parent.open_board(self.parent.flag)


class Create_column(Frame):
    # Конструктор этого класса поддерживает дополнительный параметр parent, с которым передается ссылка на главное окно
    # Она понадобится нам, чтобы вывести занесенное значение (имя колонки) в главном окне (Axello)
    def __init__(self, master, parent):
        super(Create_column, self).__init__(master)
        self.parent = parent  # Сохраним ссылку на главное окно в атрибуте
        self.master.title("Создать колонку")
        self.master.geometry('230x100+300+300')
        self.master.resizable(False, False)

        self.grid()
        self.get_name()

        self.focus_set()  # He забываем принудительно активизировать выведенное окно

    def get_name(self):
        # ==============================VARIABLES======================================
        self.cname = StringVar(value='')

        # ==============================LABELS=========================================

        back_lbl = Label(self, bg='#9DB0FF', width=32, height=2)
        back_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        lbl = Label(self, text='Введите название колонки\n(например, Новая колонка)', bg='#9DB0FF', fg='#03273F')
        lbl.grid(row=0, column=0, columnspan=2)

        # ==============================ENTRY WIDGETS==================================

        name_ent = Entry(self, width=36, textvariable=self.cname)
        name_ent.grid(row=1, column=0, columnspan=2, padx=[5, 5], pady=[5, 5])

        # ==============================BUTTON WIDGETS=================================

        ready_btn = Button(self, text='Создать', command=self.ready, bg='#B8D41D', fg='#515F0B')
        ready_btn.grid(row=2, column=0, sticky=W, padx=[5, 5], pady=[5, 5])

        cancel_btn = Button(self, text='Отмена', command=self.master.destroy, bg='#F08080', fg='#800000')
        cancel_btn.grid(row=2, column=1, sticky=E, padx=[5, 5], pady=[5, 5])

    def ready(self):
        self.master.destroy()

        c_name = self.cname.get()
        b_id = self.parent.id

        db.insert_column(c_name, b_id)

        self.parent.open_board(self.parent.flag)
