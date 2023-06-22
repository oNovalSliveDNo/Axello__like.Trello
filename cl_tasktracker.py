from tkinter import *
from PIL import Image, ImageTk
from functools import partial

from database import db
from classes import User, Board, Column, Card

image1 = 'login.png'
image2 = 'all_boards.png'
image3 = 'board.png'


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


class TaskTracker(Frame):
    def __init__(self, master):
        super(TaskTracker, self).__init__(master)

        self.grid()
        self.create_login_widgets()

    def create_login_widgets(self):
        self.a = self.canvases(image1)

        # ==============================VARIABLES======================================

        self.USERNAME_LOG = StringVar()
        self.PASSWORD_LOG = StringVar()
        self.USERNAME_REG = StringVar()
        self.PASSWORD1_REG = StringVar()
        self.PASSWORD2_REG = StringVar()

        # ==============================LABELS=========================================

        self.error_lbl = Label(self.a, text='', bg='#ECF3F9', fg='#FF0000')
        self.error_lbl.place(x=730, y=552)

        # ==============================ENTRY WIDGETS==================================

        self.u_log = Entry(self.a, textvariable=self.USERNAME_LOG, font=(7), bg='white', fg='orange', width=18)
        self.u_log.place(x=580, y=360)
        self.p_log = Entry(self.a, textvariable=self.PASSWORD_LOG, show="*", font=(7), bg='white', fg='purple', width=18)
        self.p_log.place(x=580, y=415)

        self.u_reg = Entry(self.a, textvariable=self.USERNAME_REG, font=(7), bg='white', fg='orange', width=18)
        self.u_reg.place(x=840, y=360)
        self.p_reg1 = Entry(self.a, textvariable=self.PASSWORD1_REG, show="*", font=(7), bg='white', fg='purple', width=18)
        self.p_reg1.place(x=840, y=415)
        self.p_reg2 = Entry(self.a, textvariable=self.PASSWORD2_REG, show="*", font=(7), bg='white', fg='purple', width=18)
        self.p_reg2.place(x=840, y=470)

        # ==============================BUTTON WIDGETS=================================

        self.log_bttn = Button(self.a, text="ВОЙТИ", font='15', width=16, bg='#54D9D5', fg='#03273F', command=self.check_aut_log_pas)
        self.log_bttn.place(x=583, y=455)

        self.reg_bttn = Button(self.a, text="Создать аккаунт", font='15', width=16, bg='#54D9D5', fg='#03273F', command=self.check_reg_log_pas)
        self.reg_bttn.place(x=843, y=506)

    def create_menu_widgets(self):
        self.a.forget()
        self.b = self.canvases(image2)

        # ==============================VARIABLES======================================

        self.names_of_user_boards = list(board.name for board in db.user_objects[-1].owner_board_objects)
        self.names_of_party_boards = list(str(board.name) for board in db.user_objects[-1].party_board_objects)
        self.names_of_important_boards = list(str(board.name) for board in db.user_objects[-1].important_board_objects)
        self.names_of_public_boards = list(str(board.name) for board in db.user_objects[-1].public_board_objects)

        # ==============================LISTBOX WIDGETS================================

        self.your_boards = Listbox(self.b, listvariable=StringVar(value=self.names_of_user_boards), font='15', width=16, height=15)
        self.your_boards.place(x=330, y=280)

        self.your_boards1 = Listbox(self.b, listvariable=StringVar(value=self.names_of_party_boards), font='15', width=16, height=15)
        self.your_boards1.place(x=555, y=280)

        self.your_boards2 = Listbox(self.b, listvariable=StringVar(value=self.names_of_important_boards), font='15', width=16, height=15)
        self.your_boards2.place(x=780, y=280)

        self.your_boards3 = Listbox(self.b, listvariable=StringVar(value=self.names_of_public_boards), font='15', width=16, height=15)
        self.your_boards3.place(x=1005, y=280)

        # ==============================SCROLL WIDGETS=================================

        self.scrollbar_your_boards = Scrollbar(self.b, orient="vertical", command=self.your_boards.yview)
        self.scrollbar_your_boards.place(x=513, y=280, height=360)
        self.your_boards["yscrollcommand"] = self.scrollbar_your_boards.set

        self.scrollbar_your_boards1 = Scrollbar(self.b, orient="vertical", command=self.your_boards1.yview)
        self.scrollbar_your_boards1.place(x=738, y=280, height=360)
        self.your_boards1["yscrollcommand"] = self.scrollbar_your_boards1.set

        self.scrollbar_your_boards2 = Scrollbar(self.b, orient="vertical", command=self.your_boards2.yview)
        self.scrollbar_your_boards2.place(x=963, y=280, height=360)
        self.your_boards2["yscrollcommand"] = self.scrollbar_your_boards2.set

        self.scrollbar_your_boards3 = Scrollbar(self.b, orient="vertical", command=self.your_boards3.yview)
        self.scrollbar_your_boards3.place(x=1188, y=280, height=360)
        self.your_boards3["yscrollcommand"] = self.scrollbar_your_boards3.set

        # ==============================BUTTON WIDGETS=================================

        self.new_board = Button(self.b, text='НОВАЯ ДОСКА', font='Calibri 15', height=3, width=15, bg='#92D050', command=self.create_board)
        self.new_board.place(x=277, y=97)

        self.back = Button(self.b, text='НАЗАД', font='Calibri 15', width=15, bg='#F08080', command=self.create_login_widgets)
        self.back.place(x=450, y=120)

        self.bttn = Button(self.b, text='ОТКРЫТЬ', font='Calibri 15', bg='#92D050', fg='#32501B', width=20, command=partial(self.open_board, 1))
        self.bttn.place(x=326, y=655)

        self.bttn = Button(self.b, text='УДАЛИТЬ', font='Calibri 15', bg='#F4B183', fg='#843C0C', width=20, command=self.delete_board)
        self.bttn.place(x=326, y=700)

        self.bttn = Button(self.b, text='ОТКРЫТЬ', font='Calibri 15', bg='#92D050', fg='#32501B', width=20, command=partial(self.open_board, 2))
        self.bttn.place(x=551, y=655)

        self.bttn = Button(self.b, text='ОТКРЫТЬ', font='Calibri 15', bg='#92D050', fg='#32501B', width=20, command=partial(self.open_board, 3))
        self.bttn.place(x=775, y=655)

        self.bttn = Button(self.b, text='ОТКРЫТЬ', font='Calibri 15', bg='#92D050', fg='#32501B', width=20, command=partial(self.open_board, 4))
        self.bttn.place(x=1000, y=655)

    # ==============================BOARD METHODS==================================

    def open_board(self, flag: int):
        if flag == 1:
            selection = self.your_boards.curselection()
            board_lst = db.user_objects[-1].owner_board_objects
        elif flag == 2:
            selection = self.your_boards1.curselection()
            board_lst = db.user_objects[-1].party_board_objects
        elif flag == 3:
            selection = self.your_boards2.curselection()
            board_lst = db.user_objects[-1].important_board_objects
        elif flag == 4:
            selection = self.your_boards3.curselection()
            board_lst = db.user_objects[-1].public_board_objects

        if len(board_lst) > 0 and len(selection) > 0:
            self.a.forget()
            self.b.forget()
            self.c = self.canvases(image3)
            name = board_lst[selection[0]].name
            self.id = board_lst[selection[0]].board_id

            # ==============================LABEL WIDGETS==================================

            self.name = Label(self.c, text=name, font='Calibri 17', bg='#FFE699')
            self.name.place(x=391, y=673)

            # ==============================RADIO BUTTON WIDGETS===========================

            self.important = Checkbutton(self.c, text='Избранное', font='Calibri 17', bg='#FFC728')
            self.important.place(x=1026, y=670)

            # ==============================BUTTON WIDGETS=================================

            self.new_name = Button(self.c, text='Переименовать', font='Calibri 17', bg='#FFC728', command=partial(self.rename_board, self.id, flag))
            self.new_name.place(x=847, y=667)

            self.invite = Button(self.c, text='Пригласить', font='Calibri 17', width=11, bg='#FFC728')
            self.invite.place(x=1175, y=667)

            self.back = Button(self.c, text='НАЗАД', font='Calibri 17', width=14, fg='#7F6000', bg='#F4B183', command=self.create_menu_widgets)
            self.back.place(x=1325, y=667)

            for board in board_lst:
                start_x = 400

                if (board.board_id == self.id) and (len(board.columns) == 0):
                    self.bttn = Button(self.c, text='Новая колонка', font='Calibri 17', bg='#A9D18E', fg='#385723', width=21, height=18,
                                       command=partial(self.create_column, flag)).place(x=start_x, y=65)

                elif (board.board_id == self.id) and (0 < len(board.columns) < 5):
                    count = 0

                    for column in board.columns:
                        # ==============================VARIABLES======================================

                        self.name_of_cards = [card.name for card in column.cards]
                        self.name_of_card_var = StringVar(value=self.name_of_cards)

                        # ==============================LABEL WIDGETS==================================

                        self.lbl = Label(self.c, font='Calibri 17', bg='#EDEDED', fg='#3A3C40', width=21, height=20)
                        self.lbl.place(x=start_x + 277 * count, y=65)

                        # ==============================ENTRY WIDGETS==================================

                        self.card_entry = Entry(self.c, font='Calibri 14', bg='#FFFFFF', fg='#000000', width=15)
                        self.card_entry.place(x=start_x + 5 + 277 * count, y=110)

                        # ==============================LISTBOX WIDGETS================================

                        self.lst_column = Listbox(self.c, listvariable=self.name_of_card_var, font='Calibri 14', bg='#FFFFFF',
                                                  fg='#000000', width=22, height=19)
                        self.lst_column.place(x=start_x + 5 + 277 * count, y=140)
                        # ==============================SCROLL WIDGETS=================================

                        self.scrollbar = Scrollbar(self.c, orient="vertical", command=self.lst_column.yview)
                        self.scrollbar.place(x=start_x + 237 + 277 * count, y=137, height=467)
                        self.lst_column["yscrollcommand"] = self.scrollbar.set

                        # ==============================BUTTON WIDGETS=================================

                        self.bttn = Button(self.c, text=column.name, font='Calibri 14', bg='#54D9D5', fg='#03273F', width=13, height=1,
                                           command=partial(self.rename_column, column.column_id, flag))
                        self.bttn.place(x=start_x + 277 * count, y=65)

                        self.bttn = Button(self.c, text=' X ', bg='#F08080', fg='#800000',
                                           command=partial(self.delete_column, column.column_id, flag))
                        self.bttn.place(x=start_x + 230 + 277 * count, y=70)

                        self.bttn = Button(self.c, text='Добавить', font='Calibri 11', bg='#A9D18E', fg='#385723', command=partial(
                            self.create_card, column.column_id, flag))
                        self.bttn.place(x=start_x + 180 + 277 * count, y=107)

                        self.bttn = Button(self.c, text='Удалить', font='Calibri 10', bg='#F08080', fg='#800000', command=partial(
                            self.delete_card, column.cards, flag))
                        self.bttn.place(x=start_x + 200 + 277 * count, y=601)

                        self.bttn = Button(self.c, text='Переименовать', font='Calibri 10', bg='#FFC728', fg='#000000', command=partial(
                            self.rename_card, column.cards, flag))
                        self.bttn.place(x=start_x + 3 + 277 * count, y=601)

                        self.bttn = Button(self.c, text='Переместить', font='Calibri 10', bg='#FFC728', fg='#000000')
                        self.bttn.place(x=start_x + 103 + 277 * count, y=601)

                        count += 1

                    if len(board.columns) < 4:
                        self.bttn = Button(self.c, text='Новая колонка', font='Calibri 17', bg='#A9D18E', fg='#385723', width=21, height=18,
                                           command=partial(self.create_column, flag))
                        self.bttn.place(x=start_x + 277 * len(board.columns), y=65)
                else:
                    continue

    def create_board(self):
        self.board_name = ''
        self.board_type = ''

        # Выводим вторичное окно, не забыв указать в параметре parent конструктора ссылку на главное окно
        Create_board(master=Toplevel(), parent=self)

    def rename_board(self, board_id: int, flag: int):
        self.board_id = board_id
        self.flag = flag

        # Выводим вторичное окно, не забыв указать в параметре parent конструктора ссылку на главное окно
        Rename_board(master=Toplevel(), parent=self)

    def delete_board(self):
        selection = self.your_boards.curselection()
        if len(db.user_objects[-1].owner_board_objects) > 0 and len(selection) > 0:
            b_id = db.user_objects[-1].owner_board_objects[selection[0]].board_id
            db.delete_board(b_id)
            self.create_menu_widgets()

    # ==============================COLUMN METHODS=================================

    def create_column(self, flag: int):
        self.flag = flag

        # Выводим вторичное окно, не забыв указать в параметре parent конструктора ссылку на главное окно
        Create_column(master=Toplevel(), parent=self)

    def rename_column(self, column_id: int, flag: int):
        self.column_id = column_id
        self.flag = flag

        # Выводим вторичное окно, не забыв указать в параметре parent конструктора ссылку на главное окно
        Rename_column(master=Toplevel(), parent=self)

    def delete_column(self, column_id: int, flag: int):
        db.delete_column(column_id)
        self.open_board(flag)

    # ==============================CARD METHODS===================================

    def create_card(self, column_id: int, flag: int):
        self.new_card = self.card_entry.get()

        user_id = db.user_objects[-1].user_id
        db.insert_card(self.new_card, 1, column_id, user_id)

        self.open_board(flag)

    def rename_card(self, cards, flag: int):
        selection = self.lst_column.curselection()
        self.card_id = cards[selection[0]].card_id
        self.flag = flag

        # Выводим вторичное окно, не забыв указать в параметре parent конструктора ссылку на главное окно
        Rename_card(master=Toplevel(), parent=self)

    def delete_card(self, cards, flag: int):
        selection = self.lst_column.curselection()
        card_id = cards[selection[0]].card_id
        db.delete_card(card_id)
        self.open_board(flag)

    # ==============================METHODS========================================

    def canvases(self, images):
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()

        photo = Image.open(images)
        photo1 = photo.resize((w, h), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(photo1)

        self.canvas = Canvas(self, width='%d' % w, height='%d' % h)
        self.canvas.grid(row=0, column=0)
        self.canvas.grid_propagate(0)
        self.canvas.create_image(0, 0, anchor=NW, image=photo2)
        self.canvas.image = photo2
        return self.canvas

    def check_reg_log_pas(self):
        u_name = self.USERNAME_REG.get()
        u_password1 = self.PASSWORD1_REG.get()
        u_password2 = self.PASSWORD2_REG.get()

        if (u_name == '') or (u_password1 == '') or (u_password2 == ''):
            self.error_lbl.config(text='Вы не ввели логин или пароль!')

        elif (u_password1 != u_password2):
            self.error_lbl.config(text='Пароли не совпадают!')

        elif (len(u_name) < 4):
            self.error_lbl.config(text='Логин должен состоять хотя бы из 4 символов')

        elif (len(u_password1) < 6) or (len(u_password2) < 6):
            self.error_lbl.config(text='Пароль должен состоять хотя бы из 6 символов')

        elif (len(u_name) > 50):
            self.error_lbl.config(text='Логин не должен превышать 50 символов')

        elif (len(u_password1) > 50) or (len(u_password2) > 50):
            self.error_lbl.config(text='Пароль не должен превышать 50 символов')

        elif db.username_relevant(u_name) == False:
            self.error_lbl.config(text='Данное имя пользователя уже занято')

        else:
            user = User(u_name, u_password2)
            db.user_objects.append(user)
            user.user_id = int(db.insert_user(user.username, user.password))

            db.initializated_owner_board_objects(user.user_id)
            db.initializated_party_board_objects(user.user_id)
            db.initializated_important_board_objects(user.user_id)
            db.initializated_public_board_objects(user.user_id)

            self.create_menu_widgets()

    def check_aut_log_pas(self):
        u_name = self.USERNAME_LOG.get()
        u_password = self.PASSWORD_LOG.get()

        if db.user_validated(u_name, u_password) == False:
            self.error_lbl.config(text='Неверный логин / пароль')

        else:
            user = User(u_name, u_password)
            db.user_objects.append(user)
            user.user_id = int(db.get_user_id_from_user_name(user.username))

            db.initializated_owner_board_objects(user.user_id)
            db.initializated_party_board_objects(user.user_id)
            db.initializated_important_board_objects(user.user_id)
            db.initializated_public_board_objects(user.user_id)

            self.create_menu_widgets()
