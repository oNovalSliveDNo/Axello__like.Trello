from tkinter import *


class Board():
    def __init__(self, name:str, btype:str):
        self.name = name
        self.type = btype
        self.columns = []
        self.owner = None

    def create_board_menu_widgets(self, start_x:int):
        self.start_x = start_x

        self.back_lbl = Label(bg='#9DB0FF', width=214, height=3)
        self.back_lbl.grid(row=1, column=0, columnspan=11, sticky=NW)

        self.name_lbl = Label(text='название доски', height=2, bg='#9DB0FF', fg='#03273F')
        self.name_lbl.place(x=5, y=55)

        self.delete_board_bttn = Button(text='Удалить доску', height=2, bg='#F08080', fg='#800000')
        self.delete_board_bttn.place(x=220, y=55)

        self.rename_board_bttn = Button(text='Переименовать', height=2, bg='#B1D2E7', fg='#03273F')
        self.rename_board_bttn.place(x=315, y=55)

        self.add_to_favour_bttn = Checkbutton(text='Избранное', height=2, bg='#B1D2E7', fg='#03273F')
        self.add_to_favour_bttn.place(x=420, y=55)

        self.invite_bttn = Button(text='Пригласить', height=2, bg='#B1D2E7', fg='#03273F')
        self.invite_bttn.place(x=1345, y=55)

        self.persons_bttn = Button(text='Участники', height=2, bg='#B1D2E7', fg='#03273F')
        self.persons_bttn.place(x=1427, y=55)

    def rename_board(self):
        self.name = input('Введите новое название для доски:')
