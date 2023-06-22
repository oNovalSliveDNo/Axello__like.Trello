from tkinter import *
from cl_tasktracker import TaskTracker

if __name__ == '__main__':
    # создание нового окна
    root = Tk()
    root.title('Axello')
    root.state('zoomed')

    # создание рамки для размещения элементов
    app = TaskTracker(root)

    # старт событийного цикла
    root.mainloop()
