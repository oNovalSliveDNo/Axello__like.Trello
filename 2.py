def open_board(self, flag: int):
    if flag == 1:
        selection = self.your_boards.curselection()
        board_lst = db.user_objects[-1].owner_board_objects
    elif flag == 2:
        selection = self.your_boards1.curselection()
        board_lst = db.user_objects[-1].party_board_objects
    elif flag == 3:
        selection = self.your_boards2.curselection()
        board_lst = db.user_objects[-1].important_board_objects
    elif flag == 4:
        selection = self.your_boards3.curselection()
        board_lst = db.user_objects[-1].public_board_objects

    if len(board_lst) > 0 and len(selection) > 0:
        self.a.forget()
        self.b.forget()
        self.c = self.canvases(image3)
        name = board_lst[selection[0]].name
        self.id = board_lst[selection[0]].board_id

        # ==============================LABEL WIDGETS==================================

        self.name = Label(self.c, text=name, font='Calibri 17', bg='#FFE699')
        self.name.place(x=391, y=673)

        # ==============================RADIO BUTTON WIDGETS===========================

        self.important = Checkbutton(self.c, text='Избранное', font='Calibri 17', bg='#FFC728')
        self.important.place(x=1026, y=670)

        # ==============================BUTTON WIDGETS=================================

        self.new_name = Button(self.c, text='Переименовать', font='Calibri 17', bg='#FFC728', command=partial(self.rename_board, self.id, flag))
        self.new_name.place(x=847, y=667)

        self.invite = Button(self.c, text='Пригласить', font='Calibri 17', width=11, bg='#FFC728')
        self.invite.place(x=1175, y=667)

        self.back = Button(self.c, text='НАЗАД', font='Calibri 17', width=14, fg='#7F6000', bg='#F4B183', command=self.create_menu_widgets)
        self.back.place(x=1325, y=667)

        for board in board_lst:
            start_x = 400

            if (board.board_id == self.id) and (len(board.columns) == 0):
                self.bttn = Button(self.c, text='Новая колонка', font='Calibri 17', bg='#A9D18E', fg='#385723', width=21, height=18,
                                   command=partial(self.create_column, flag)).place(x=start_x, y=65)

            elif (board.board_id == self.id) and (0 < len(board.columns) < 5):
                count = 0

                for column in board.columns:
                    # ==============================VARIABLES======================================

                    self.name_of_cards = [card.name for card in column.cards]
                    self.name_of_card_var = StringVar(value=self.name_of_cards)

                    # ==============================LABEL WIDGETS==================================

                    self.lbl = Label(self.c, font='Calibri 17', bg='#EDEDED', fg='#3A3C40', width=21, height=20)
                    self.lbl.place(x=start_x + 277 * count, y=65)

                    # ==============================ENTRY WIDGETS==================================

                    self.card_entry = Entry(self.c, font='Calibri 14', bg='#FFFFFF', fg='#000000', width=15)
                    self.card_entry.place(x=start_x + 5 + 277 * count, y=110)

                    # ==============================LISTBOX WIDGETS================================

                    self.lst_column = Listbox(self.c, listvariable=self.name_of_card_var, font='Calibri 14', bg='#FFFFFF',
                                              fg='#000000', width=22, height=19)
                    self.lst_column.place(x=start_x + 5 + 277 * count, y=140)
                    # ==============================SCROLL WIDGETS=================================

                    self.scrollbar = Scrollbar(self.c, orient="vertical", command=self.lst_column.yview)
                    self.scrollbar.place(x=start_x + 237 + 277 * count, y=137, height=467)
                    self.lst_column["yscrollcommand"] = self.scrollbar.set

                    # ==============================BUTTON WIDGETS=================================

                    self.bttn = Button(self.c, text=column.name, font='Calibri 14', bg='#54D9D5', fg='#03273F', width=13, height=1,
                                       command=partial(self.rename_column, column.column_id, flag))
                    self.bttn.place(x=start_x + 277 * count, y=65)

                    self.bttn = Button(self.c, text=' X ', bg='#F08080', fg='#800000',
                                       command=partial(self.delete_column, column.column_id, flag))
                    self.bttn.place(x=start_x + 230 + 277 * count, y=70)

                    self.bttn = Button(self.c, text='Добавить', font='Calibri 11', bg='#A9D18E', fg='#385723', command=partial(
                        self.create_card, column.column_id, flag))
                    self.bttn.place(x=start_x + 180 + 277 * count, y=107)

                    self.bttn = Button(self.c, text='Удалить', font='Calibri 10', bg='#F08080', fg='#800000', command=partial(
                        self.delete_card, column.cards, flag))
                    self.bttn.place(x=start_x + 200 + 277 * count, y=601)

                    self.bttn = Button(self.c, text='Переименовать', font='Calibri 10', bg='#FFC728', fg='#000000', command=partial(
                        self.rename_card, column.cards, flag))
                    self.bttn.place(x=start_x + 3 + 277 * count, y=601)

                    self.bttn = Button(self.c, text='Переместить', font='Calibri 10', bg='#FFC728', fg='#000000')
                    self.bttn.place(x=start_x + 103 + 277 * count, y=601)

                    count += 1

                if len(board.columns) < 4:
                    self.bttn = Button(self.c, text='Новая колонка', font='Calibri 17', bg='#A9D18E', fg='#385723', width=21, height=18,
                                       command=partial(self.create_column, flag))
                    self.bttn.place(x=start_x + 277 * len(board.columns), y=65)
            else:
                continue


def canvases(self, images):
    w = self.winfo_screenwidth()
    h = self.winfo_screenheight()

    photo = Image.open(images)
    photo1 = photo.resize((w, h), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(photo1)

    self.canvas = Canvas(self, width='%d' % w, height='%d' % h)
    self.canvas.grid(row=0, column=0)
    self.canvas.grid_propagate(0)
    self.canvas.create_image(0, 0, anchor=NW, image=photo2)
    self.canvas.image = photo2
    return self.canvas


def check_reg_log_pas(self):
    u_name = self.USERNAME_REG.get()
    u_password1 = self.PASSWORD1_REG.get()
    u_password2 = self.PASSWORD2_REG.get()

    if (u_name == '') or (u_password1 == '') or (u_password2 == ''):
        self.error_lbl.config(text='Вы не ввели логин или пароль!')

    elif (u_password1 != u_password2):
        self.error_lbl.config(text='Пароли не совпадают!')

    elif (len(u_name) < 4):
        self.error_lbl.config(text='Логин должен состоять хотя бы из 4 символов')

    elif (len(u_password1) < 6) or (len(u_password2) < 6):
        self.error_lbl.config(text='Пароль должен состоять хотя бы из 6 символов')

    elif (len(u_name) > 50):
        self.error_lbl.config(text='Логин не должен превышать 50 символов')

    elif (len(u_password1) > 50) or (len(u_password2) > 50):
        self.error_lbl.config(text='Пароль не должен превышать 50 символов')

    elif db.username_relevant(u_name) == False:
        self.error_lbl.config(text='Данное имя пользователя уже занято')

    else:
        user = User(u_name, u_password2)
        db.user_objects.append(user)
        user.user_id = int(db.insert_user(user.username, user.password))

        db.initializated_owner_board_objects(user.user_id)
        db.initializated_party_board_objects(user.user_id)
        db.initializated_important_board_objects(user.user_id)
        db.initializated_public_board_objects(user.user_id)

        self.create_menu_widgets()


def check_aut_log_pas(self):
    u_name = self.USERNAME_LOG.get()
    u_password = self.PASSWORD_LOG.get()

    if db.user_validated(u_name, u_password) == False:
        self.error_lbl.config(text='Неверный логин / пароль')

    else:
        user = User(u_name, u_password)
        db.user_objects.append(user)
        user.user_id = int(db.get_user_id_from_user_name(user.username))

        db.initializated_owner_board_objects(user.user_id)
        db.initializated_party_board_objects(user.user_id)
        db.initializated_important_board_objects(user.user_id)
        db.initializated_public_board_objects(user.user_id)

        self.create_menu_widgets()
