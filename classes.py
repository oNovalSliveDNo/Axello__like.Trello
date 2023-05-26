from tkinter import *


class Application(Frame):
    """Инициализируем рамку"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_headline_widgets()

    def create_headline_widgets(self):
        """Создание кнопок в шапке"""
        bttn_img = Button(self, text='⊞')
        bttn_name = Button(self, text='Axello')
        bttn_workspaces = Button(self, text='Рабочие пространства  ⮟ ')
        bttn_recent = Button(self, text='Недавние  ⮟ ')
        bttn_favourites = Button(self, text='В избранном  ⮟ ')
        bttn_templates = Button(self, text='Шаблоны  ⮟ ')
        bttn_create = Button(self, text='Создать')

        self.srch_lbl = Label(self, text='Поиск : ')
        self.srch_ent = Entry(self)
        bttn_notifications = Button(self, text='Уведомления')
        bttn_information = Button(self, text='Информация')
        bttn_theme = Button(self, text='Тема')
        bttn_profile = Button(self, text='Профиль')

        bttn_img.grid(row=0, column=0)
        bttn_name.grid(row=0, column=1)
        bttn_workspaces.grid(row=0, column=2)
        bttn_recent.grid(row=0, column=3)
        bttn_favourites.grid(row=0, column=4)
        bttn_templates.grid(row=0, column=5)
        bttn_create.grid(row=0, column=6, columnspan=4)

        self.srch_lbl.grid(row=0, column=10, padx=[545, 0])
        self.srch_ent.grid(row=0, column=11)
        bttn_notifications.grid(row=0, column=12)
        bttn_information.grid(row=0, column=13)
        bttn_theme.grid(row=0, column=14)
        bttn_profile.grid(row=0, column=15)
