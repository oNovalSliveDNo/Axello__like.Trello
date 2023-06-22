class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_id = None
        self.owner_board_objects = list()
        self.party_board_objects = list()
        self.important_board_objects = list()
        self.public_board_objects = list()


class Board():
    def __init__(self, name: str, btype: str, important: bool):
        self.name = name
        self.type = btype
        self.important = important
        self.board_id = None
        self.columns = list()


class Column():
    def __init__(self, column_name: str):
        self.name = column_name
        self.column_id = None
        self.cards = list()


class Card():
    def __init__(self, name: str, sequence_number: int):
        self.name = name
        self.sequence_number = sequence_number
        self.card_id = None
