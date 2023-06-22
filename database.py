import psycopg2
from classes import Board, Column, Card


class Database():
    def __init__(self):
        self.DATABASE = 'axellodb'
        self.PASSWORD = 'AmongGT8'  # GTA4586AmongGT8
        self.user_objects = list()

    def connected(self):
        """Подключение к базе данных"""
        try:
            self.con = psycopg2.connect(database=self.DATABASE,
                                        user="postgres",
                                        password=self.PASSWORD,
                                        host="127.0.0.1",
                                        port="5432")

            print(f'Database "{self.DATABASE}" opened successfully')
            return True

        except:
            print(f'Database "{self.DATABASE}" is not opened')
            return False

    def username_relevant(self, username: str):
        """Проверить на актуальность имя пользователя"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("SELECT user_name FROM users")

            rows = cursor.fetchall()

            for row in rows:
                if username == row[0]:
                    self.con.close()
                    return False

            self.con.close()
            return True

    def user_validated(self, username: str, password: str):
        """Проверить на валидацию логина и пароля"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("SELECT user_name, user_password FROM users")

            rows = cursor.fetchall()

            for row in rows:
                if username == row[0] and password == row[1]:
                    self.con.close()
                    return True

            self.con.close()
            return False

    def get_user_id_from_user_name(self, username: str):
        """получим user_id, зная user_name"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("SELECT id FROM users WHERE user_name = '" + str(username) + "'")
            rows = cursor.fetchall()

            try:
                user_id = rows[0][0]
                self.con.close()
                return user_id

            except:
                self.con.close()

    def get_board_name_from_board_id(self, board_id: int):
        """получим board_name, зная board_id"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("SELECT name FROM boards WHERE id = '" + str(board_id) + "'")
            rows = cursor.fetchall()

            try:
                board_name = rows[0][0]
                self.con.close()
                return board_name

            except:
                self.con.close()

    def insert_user(self, username: str, password: str):
        """Внести пользователя в таблицу базы данных"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("INSERT INTO users (user_name, user_password) VALUES ('" + str(username) + "', '" + str(password) + "')")

            self.con.commit()
            self.con.close()

            user_id = self.get_user_id_from_user_name(username)

            print(f'User "{username}" inserted successfully')
            return user_id

    def initializated_owner_board_objects(self, user_id: int):
        """Подгрузка данных owner_board_objects из БД"""

        if self.connected() is True:
            # очистим список объекта класса User
            self.user_objects[-1].owner_board_objects.clear()

            # заполняем список owner_board_objects объекта класса User объектами Board (по данным из Базы Данных)
            cursor = self.con.cursor()
            cursor.execute("SELECT board_id FROM users_boards WHERE user_id = '" + str(user_id) + "'")
            rows = cursor.fetchall()

            for i in range(len(rows)):
                self.user_objects[-1].owner_board_objects.append(i)
                self.user_objects[-1].owner_board_objects[i] = rows[i][0]

            for i in range(len(self.user_objects[-1].owner_board_objects)):
                board_id = self.user_objects[-1].owner_board_objects[i]

                cursor = self.con.cursor()
                cursor.execute("SELECT name, type, important FROM boards WHERE id = '" + str(board_id) + "'")
                rows = cursor.fetchall()

                board = Board(rows[0][0], rows[0][1], rows[0][2])
                board.board_id = board_id

                self.user_objects[-1].owner_board_objects[i] = board

            # заполняем списки columns объектов класса Board объектами Column (по данным из Базы Данных)
            for board in self.user_objects[-1].owner_board_objects:
                cursor = self.con.cursor()
                cursor.execute("SELECT id FROM boards WHERE fk_creator_id = '" + str(user_id) + "' AND name = '" + str(board.name) + "'")
                rows = cursor.fetchall()

                for row in rows:
                    board_id = row[0]

                    cursor = self.con.cursor()
                    cursor.execute("SELECT id, name FROM columns WHERE fk_board_id = " + str(board_id))
                    rows = cursor.fetchall()

                    for row in rows:
                        column = Column(row[1])
                        column.column_id = row[0]
                        board.columns.append(column)

                        # заполняем списки cards объектов класса Column объектами Card (по данным из Базы Данных)
                        cursor = self.con.cursor()
                        cursor.execute("SELECT id, name, sequence_number FROM cards WHERE fk_column_id = " + str(column.column_id))
                        rows = cursor.fetchall()

                        for row in rows:
                            card = Card(row[1], row[2])
                            card.card_id = row[0]
                            column.cards.append(card)

            self.con.commit()
            self.con.close()

    def initializated_party_board_objects(self, user_id: int):
        """Подгрузка данных party_board_objects из БД"""

        if self.connected() is True:
            # очистим список объекта класса User
            self.user_objects[-1].party_board_objects.clear()

            # заполняем список party_board_objects объекта класса User объектами Board (по данным из Базы Данных)
            cursor = self.con.cursor()
            cursor.execute("SELECT board_id FROM users_boards WHERE user_id = '" + str(user_id) + "'")
            rows = cursor.fetchall()

            for i in range(len(rows)):
                self.user_objects[-1].party_board_objects.append(i)
                self.user_objects[-1].party_board_objects[i] = rows[i][0]

            for i in range(len(self.user_objects[-1].party_board_objects)):
                board_id = self.user_objects[-1].party_board_objects[i]

                cursor = self.con.cursor()
                cursor.execute("SELECT name, type, important FROM boards WHERE id = '" + str(board_id) + "'")
                rows = cursor.fetchall()

                board = Board(rows[0][0], rows[0][1], rows[0][2])
                board.board_id = board_id

                self.user_objects[-1].party_board_objects[i] = board

            # заполняем списки columns объектов класса Board объектами Column (по данным из Базы Данных)
            for board in self.user_objects[-1].party_board_objects:
                cursor = self.con.cursor()
                cursor.execute("SELECT id FROM boards WHERE fk_creator_id = '" + str(user_id) + "' AND name = '" + str(board.name) + "'")
                rows = cursor.fetchall()

                for row in rows:
                    board_id = row[0]

                    cursor = self.con.cursor()
                    cursor.execute("SELECT id, name FROM columns WHERE fk_board_id = " + str(board_id))
                    rows = cursor.fetchall()

                    for row in rows:
                        column = Column(row[1])
                        column.column_id = row[0]
                        board.columns.append(column)

                        # заполняем списки cards объектов класса Column объектами Card (по данным из Базы Данных)
                        cursor = self.con.cursor()
                        cursor.execute("SELECT id, name, sequence_number FROM cards WHERE fk_column_id = " + str(column.column_id))
                        rows = cursor.fetchall()

                        for row in rows:
                            card = Card(row[1], row[2])
                            card.card_id = row[0]
                            column.cards.append(card)

            self.con.commit()
            self.con.close()

    def initializated_important_board_objects(self, user_id: int):
        """Подгрузка данных important_board_objects из БД"""

        if self.connected() is True:
            # очистим список объекта класса User
            self.user_objects[-1].important_board_objects.clear()

            # заполняем список important_board_objects объекта класса User числами (по кол-ву его избранных досок в Базе Данных)
            cursor = self.con.cursor()
            cursor.execute("SELECT COUNT (*) FROM boards WHERE important = true AND fk_creator_id = '" + str(user_id) + "'")
            rows = cursor.fetchall()
            count_important_board_objects = rows[0][0]

            for i in range(count_important_board_objects):
                self.user_objects[-1].owner_board_objects.append(i)

            # заполняем список important_board_objects объекта класса User объектами Board (по данным из Базы Данных)
            cursor = self.con.cursor()
            cursor.execute("SELECT id, name, type, important FROM boards WHERE important = true AND fk_creator_id = '" + str(user_id) + "'")
            rows = cursor.fetchall()

            for i in range(len(rows)):
                board = Board(rows[i][1], rows[i][2], rows[i][3])
                board.board_id = rows[0][0]

                self.user_objects[-1].important_board_objects[i] = board

            # заполняем списки columns объектов класса Board объектами Column (по данным из Базы Данных)
            for board in self.user_objects[-1].important_board_objects:
                cursor = self.con.cursor()
                cursor.execute("SELECT id FROM boards WHERE fk_creator_id = '" + str(user_id) + "' AND name = '" + str(board.name) + "'")
                rows = cursor.fetchall()

                for row in rows:
                    board_id = row[0]

                    cursor = self.con.cursor()
                    cursor.execute("SELECT id, name FROM columns WHERE fk_board_id = " + str(board_id))
                    rows = cursor.fetchall()

                    for row in rows:
                        column = Column(row[1])
                        column.column_id = row[0]
                        board.columns.append(column)

                        # заполняем списки cards объектов класса Column объектами Card (по данным из Базы Данных)
                        cursor = self.con.cursor()
                        cursor.execute("SELECT id, name, sequence_number FROM cards WHERE fk_column_id = " + str(column.column_id))
                        rows = cursor.fetchall()

                        for row in rows:
                            card = Card(row[1], row[2])
                            card.card_id = row[0]
                            column.cards.append(card)

            self.con.commit()
            self.con.close()

    def initializated_public_board_objects(self, user_id: int):
        """Подгрузка данных public_board_objects из БД"""

        if self.connected() is True:
            # очистим список объекта класса User
            self.user_objects[-1].public_board_objects.clear()

            # заполняем список public_board_objects объекта класса User объектами Board (по данным из Базы Данных)
            cursor = self.con.cursor()
            cursor.execute("SELECT COUNT (*) FROM boards WHERE type = 'Общественная'")
            rows = cursor.fetchall()
            count_public_board_objects = rows[0][0]

            for i in range(count_public_board_objects):
                self.user_objects[-1].public_board_objects.append(i)

            # заполняем список public_board_objects объекта класса User объектами Board (по данным из Базы Данных)
            cursor = self.con.cursor()
            cursor.execute("SELECT id, name, type, important FROM boards WHERE type = 'Общественная'")
            rows = cursor.fetchall()

            for i in range(len(rows)):
                board = Board(rows[i][1], rows[i][2], rows[i][3])
                board.board_id = rows[0][0]

                self.user_objects[-1].public_board_objects[i] = board

            # заполняем списки columns объектов класса Board объектами Column (по данным из Базы Данных)
            for board in self.user_objects[-1].public_board_objects:
                cursor = self.con.cursor()
                cursor.execute("SELECT id FROM boards WHERE fk_creator_id = '" + str(user_id) + "' AND name = '" + str(board.name) + "'")
                rows = cursor.fetchall()

                for row in rows:
                    board_id = row[0]

                    cursor = self.con.cursor()
                    cursor.execute("SELECT id, name FROM columns WHERE fk_board_id = " + str(board_id))
                    rows = cursor.fetchall()

                    for row in rows:
                        column = Column(row[1])
                        column.column_id = row[0]
                        board.columns.append(column)

                        # заполняем списки cards объектов класса Column объектами Card (по данным из Базы Данных)
                        cursor = self.con.cursor()
                        cursor.execute("SELECT id, name, sequence_number FROM cards WHERE fk_column_id = " + str(column.column_id))
                        rows = cursor.fetchall()

                        for row in rows:
                            card = Card(row[1], row[2])
                            card.card_id = row[0]
                            column.cards.append(card)

            self.con.commit()
            self.con.close()

    def change_username(self, user_id: int, new_username: str):
        """Изменить имя пользователя в таблице"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("UPDATE users set user_name = '" + str(new_username) + "' where id = " + str(user_id))
            self.con.commit()
            self.con.close()

            self.initializated_owner_board_objects(user_id)
            self.initializated_party_board_objects(user_id)
            self.initializated_important_board_objects(user_id)
            self.initializated_public_board_objects(user_id)

    def change_user_password(self, user_id: int, new_password: str):
        """Изменить пароль пользователя в таблице"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("UPDATE users set user_password = '" + str(new_password) + "' where id = " + str(user_id))
            self.con.commit()
            self.con.close()

            self.initializated_owner_board_objects(user_id)
            self.initializated_party_board_objects(user_id)
            self.initializated_important_board_objects(user_id)
            self.initializated_public_board_objects(user_id)

    def delete_user(self, user_id):
        """Удалить пользователя из таблицы"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("DELETE FROM users_boards WHERE user_id = " + str(user_id))
            self.con.commit()

            cursor.execute("DELETE FROM users WHERE id = " + str(user_id))
            self.con.commit()

            self.con.close()

            self.initializated_owner_board_objects(user_id)
            self.initializated_party_board_objects(user_id)
            self.initializated_important_board_objects(user_id)
            self.initializated_public_board_objects(user_id)

            return True

        else:
            print(f'Database "{self.DATABASE}" is not opened')
            return False

    def insert_board(self, board_name: str, board_type: str, user_id: int):
        """Внести доску в таблицу базы данных"""

        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("INSERT INTO boards (name, type, important, fk_creator_id) VALUES ('" + str(board_name) + "', '" + str(board_type) + \
                           "', false, " + str(user_id) + ")")
            self.con.commit()

            cursor = self.con.cursor()
            cursor.execute("SELECT id FROM boards WHERE name = '" + str(board_name) + "'")
            rows = cursor.fetchall()
            board_id = rows[-1][0]

            cursor = self.con.cursor()
            cursor.execute("INSERT INTO users_boards (user_id, board_id) VALUES (" + str(user_id) + ", " + str(board_id) + ")")

            self.con.commit()
            self.con.close()

            self.initializated_owner_board_objects(user_id)
            self.initializated_party_board_objects(user_id)
            self.initializated_important_board_objects(user_id)
            self.initializated_public_board_objects(user_id)

        else:
            print(f'Database "{self.DATABASE}" is not opened')
            return False

    def change_board_name(self, board_id: int, new_name: str):
        """Изменить название доски в таблице"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("UPDATE boards set name = '" + str(new_name) + "' where id = " + str(board_id))
            self.con.commit()
            self.con.close()

            self.initializated_owner_board_objects(self.user_objects[-1].user_id)
            self.initializated_party_board_objects(self.user_objects[-1].user_id)
            self.initializated_important_board_objects(self.user_objects[-1].user_id)
            self.initializated_public_board_objects(self.user_objects[-1].user_id)

            return True

    def delete_board(self, board_id: int):
        """Удалить доску из таблицы"""

        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("DELETE FROM users_boards WHERE board_id = " + str(board_id))
            self.con.commit()

            cursor.execute("DELETE FROM boards WHERE id = " + str(board_id))
            self.con.commit()

            self.con.close()

            self.initializated_owner_board_objects(self.user_objects[-1].user_id)
            self.initializated_party_board_objects(self.user_objects[-1].user_id)
            self.initializated_important_board_objects(self.user_objects[-1].user_id)
            self.initializated_public_board_objects(self.user_objects[-1].user_id)

            return True

        else:
            print(f'Database "{self.DATABASE}" is not opened')
            return False

    def insert_column(self, column_name: str, board_id: int):
        """Внести колонку в таблицу базы данных"""

        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("INSERT INTO columns (name, fk_board_id) VALUES ('" + str(column_name) + "', " + str(board_id) + ")")

            self.con.commit()
            self.con.close()

            self.initializated_owner_board_objects(self.user_objects[-1].user_id)
            self.initializated_party_board_objects(self.user_objects[-1].user_id)
            self.initializated_important_board_objects(self.user_objects[-1].user_id)
            self.initializated_public_board_objects(self.user_objects[-1].user_id)

        else:
            print(f'Database "{self.DATABASE}" is not opened')
            return False

    def change_column_name(self, column_id: int, new_name: str):
        """Изменить название колонки в таблице"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("UPDATE columns set name = '" + str(new_name) + "' where id = " + str(column_id))
            self.con.commit()
            self.con.close()

            self.initializated_owner_board_objects(self.user_objects[-1].user_id)
            self.initializated_party_board_objects(self.user_objects[-1].user_id)
            self.initializated_important_board_objects(self.user_objects[-1].user_id)
            self.initializated_public_board_objects(self.user_objects[-1].user_id)

    def delete_column(self, column_id: int):
        """Удалить колонку из таблицы"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("DELETE FROM columns WHERE id = " + str(column_id))
            self.con.commit()

            self.con.close()

            self.initializated_owner_board_objects(self.user_objects[-1].user_id)
            self.initializated_party_board_objects(self.user_objects[-1].user_id)
            self.initializated_important_board_objects(self.user_objects[-1].user_id)
            self.initializated_public_board_objects(self.user_objects[-1].user_id)

            return True

        else:
            print(f'Database "{self.DATABASE}" is not opened')
            return False

    def insert_card(self, card_name: str, sequence_number: int, column_id: int, user_id: int):
        """Внести карточку в таблицу базы данных"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("INSERT INTO cards (name, sequence_number, fk_column_id, fk_creator_id) VALUES ('" \
                           + str(card_name) + "', " + str(sequence_number) + ", " + str(column_id) + ", " + str(user_id) + ")")

            self.con.commit()
            self.con.close()

            self.initializated_owner_board_objects(self.user_objects[-1].user_id)
            self.initializated_party_board_objects(self.user_objects[-1].user_id)
            self.initializated_important_board_objects(self.user_objects[-1].user_id)
            self.initializated_public_board_objects(self.user_objects[-1].user_id)

    def change_card_name(self, card_id: int, new_name: str):
        """Изменить название карточки в таблице"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("UPDATE cards set name = '" + str(new_name) + "' where id = " + str(card_id))
            self.con.commit()
            self.con.close()

            self.initializated_owner_board_objects(self.user_objects[-1].user_id)
            self.initializated_party_board_objects(self.user_objects[-1].user_id)
            self.initializated_important_board_objects(self.user_objects[-1].user_id)
            self.initializated_public_board_objects(self.user_objects[-1].user_id)

    def delete_card(self, card_id: int):
        """Удалить карточку из таблицы"""
        if self.connected() is True:
            cursor = self.con.cursor()
            cursor.execute("DELETE FROM cards WHERE id = " + str(card_id))
            self.con.commit()
            self.con.close()

            self.initializated_owner_board_objects(self.user_objects[-1].user_id)
            self.initializated_party_board_objects(self.user_objects[-1].user_id)
            self.initializated_important_board_objects(self.user_objects[-1].user_id)
            self.initializated_public_board_objects(self.user_objects[-1].user_id)

            return True

        else:
            print(f'Database "{self.DATABASE}" is not opened')
            return False


# Подключаем базу данных
db = Database()
