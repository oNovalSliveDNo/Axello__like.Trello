from cl_tasktracker import *

class Board():
    def __init__(self, owner: str, name: str, btype: str, start_x: int, width_of_column: int):
        self.name = name
        self.type = btype
        self.start_x = start_x
        self.width_of_column = width_of_column
        self.owner = owner
        self.columns = []

    def create_board_widgets(self):
        self.new_list_bttn = Button(text='    +    ', height=2, bg='#B8D41D', fg='#515F0B')
        self.new_list_bttn.place(x=self.start_x, y=110)

        self.back_lbl = Label(text=' ', bg='#9DB0FF', width=214, height=3)
        self.back_lbl.grid(row=1, column=0, columnspan=11, sticky=NW)

        self.name_lbl = Label(text=self.name, height=2, font='11', bg='#9DB0FF', fg='#03273F')
        self.name_lbl.place(y=50)

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
        self.name = input('Введите название доски (например, Новая доска)')

    def create_column(self):
        pass