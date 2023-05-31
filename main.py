from tkinter import *
from classes import *

if __name__ == '__main__':

    # создание базового окна
    root = Tk()
    root.title('Axello')
    root.geometry('1500x900+10+10')
    root.resizable(False, False)
    root.config(bg='#E0E0E0')

    # создание рамки для размещения элементов
    app = Back(root)
    app = Menu(root)
    app = Scnd_menu(root)


    # старт событийного цикла
    root.mainloop()
