class Card():
    def __init__(self, name, description, checklist):
        self.name = name
        self.description = description
        self.checklist = checklist

    def create_card(self):
        pass

    def rename_card(self):
        self.name = input('Введите новое название для карточки:')