from tkinter import *
import customtkinter
from classes import Application, Back

if __name__ == '__main__':

    # создание базового окна
    root = Tk()
    root.title('Axello')
    root.geometry('1500x900+10+10')
    root.resizable(False, False)

    # создание рамки для размещения элементов
    app = Back(root)
    app = Application(root)
    root.config(bg='#E0E0E0')

    # старт событийного цикла
    root.mainloop()
