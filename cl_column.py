class Column():
    def __init__(self, name):
        self.name = name
        self.cards = []

    def create_column(self):
        pass

    def rename_column(self):
        self.name = input('Введите новое название для столбца:')