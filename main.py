from tkinter import *
from tkinter import messagebox


# create functions
def newTask():
    task = my_entry.get()
    if task != '':
        lb.insert(END, task)
        my_entry.delete(0, 'end')
    else:
        messagebox.showwarning('warning', 'Please enter some task')


def deleteTask():
    lb.delete(ANCHOR)


# configure and create main_window
ws = Tk()
ws.geometry('500x800')
ws.title('Axello (like Trello)')
ws.config(bg='#483D8B')
ws.resizable(width=True, height=True)

# create widgets (frame, Listbox, scrollbar, Entry, button)
frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle='none'
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Task 1',
    'Task 2',
    'Task 3',
    'Task 4',
    'Task 5'
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

if __name__ == '__main__':
    # create mainloop
    ws.mainloop()
