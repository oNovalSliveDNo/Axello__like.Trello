from tkinter import *
from classes import Application

if __name__ == '__main__':
    # создание базового окна
    root = Tk()
    root.title('Axello')
    root.geometry('1500x900')

    # создание рамки для размещения элементов
    app = Application(root)

    # старт событийного цикла
    root.mainloop()
