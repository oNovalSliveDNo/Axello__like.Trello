from tkinter import *
from PIL import ImageTk, Image

class Back(Frame):
    def __init__(self, master):
        super(Back, self).__init__(master)
        self.grid()
        self.create_back_menu()


    def create_back_menu(self):
        self.back_lbl = Label(bg='#8FA0E8',width=214, height=3)
        self.back_lbl.grid(row=0, column=0, columnspan=11, sticky=NW)

        self.back_lbl = Label(bg='#9DB0FF', width=214, height=3)
        self.back_lbl.grid(row=1, column=0, columnspan=11, sticky=NW)

        self.back_lbl = Label(bg='#9DB0FF', width=7, height=55)
        self.back_lbl.grid(row=2, column=0, columnspan=11, sticky=NW)

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_menu_widgets()


    def create_menu_widgets(self):
        self.name1_lbl = Label(text='AXELLO',width=28, height=2, bg='#9DB0FF', fg='#03273F')
        self.menu1_bttn = Button(text='Меню', width=6, height=2, bg = '#F7DCBA', fg='#623803')
        self.recent1_bttn = Button(text='Недавние', height=2,bg = '#B1D2E7', fg='#03273F')
        self.favourites1_bttn = Button(text='В избранном', height=2,bg = '#B1D2E7', fg='#03273F')
        self.new_board1_bttn = Button(text='Создать', width=10, height=2,bg = '#B8D41D', fg='#515F0B')
        self.search1_bttn = Button(text='Поиск:', width=6, height=2,bg = '#B1D2E7', fg='#03273F')
        self.search1_ent = Entry(width=30,fg='#B1D2E7')
        self.notific1_bttn = Button(text='Уведомления', height=2,bg = '#B1D2E7', fg='#03273F')
        self.theme1_bttn = Button(text='Тема', width=6, height=2,bg = '#B1D2E7', fg='#03273F')
        self.profile1_bttn = Button(text='Профиль', height=2,bg = '#B1D2E7', fg='#03273F')

        self.name1_lbl.grid(row=0, column=4, columnspan=3, padx=[2, 2], pady=[5, 5])
        self.menu1_bttn.grid(row=1, column=0, padx=[2, 2], pady=[5, 5])
        self.recent1_bttn.grid(row=1, column=2, padx=[2, 2], pady=[5, 5])
        self.favourites1_bttn.grid(row=1, column=3, padx=[2, 2], pady=[5, 5])
        self.new_board1_bttn.grid(row=1, column=4, padx=[2, 2], pady=[5, 5])
        self.search1_bttn.grid(row=1, column=5, padx=[600, 2], pady=[5, 5])
        self.search1_ent.grid(row=1, column=6, padx=[2, 2], pady=[5, 5])
        self.notific1_bttn.grid(row=1, column=7, padx=[2, 2], pady=[5, 5])
        self.theme1_bttn.grid(row=1, column=8, padx=[2, 2], pady=[5, 5])
        self.profile1_bttn.grid(row=1, column=9, padx=[2, 2], pady=[5, 5])



if __name__ == '__main__':

    root = Tk()
    root.title('Axello')
    root.geometry('1500x900+10+10')
    root.resizable(False, False)

    app = Back(root)
    app = Application(root)
    root.config(bg='#E0E0E0')

    root.mainloop()