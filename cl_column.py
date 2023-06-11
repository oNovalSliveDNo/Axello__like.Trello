from tkinter import *


class Column():
    def __init__(self, column_name: str, start_x:int, width_of_column:int):
        self.name = column_name
        self.start_x = start_x
        self.width_of_column = width_of_column
        self.cards = []

        self.column_back_lbl = Label(height=51, width=self.width_of_column)
        self.column_name_lbl = Label(text=self.name)
        self.name_card_ent = Entry(width=25)
        self.add_name_card_bttn = Button(text='Добавить', bg='#B8D41D', fg='#515F0B')
        self.delete_name_card_bttn = Button(text='Удалить', bg='#F08080', fg='#800000')

    def create_column_widgets(self):
        self.column_back_lbl.place(x=self.start_x, y=110)
        self.column_name_lbl.place(x=self.start_x + 5, y=115)
        self.name_card_ent.place(x=self.start_x + 5, y=135)
        self.add_name_card_bttn.place(x=self.start_x + 165, y=132)
        self.delete_name_card_bttn.place(x=self.start_x + 170, y=850)
        self.start_x += int(self.width_of_column * 7.5)

    def rename_column(self):
        self.name = input('Введите название столбца (например, Новый столбец)')
