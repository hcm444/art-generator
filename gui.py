import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from main import generate, show, clear, generate_random, generate_all

# root window
root = tk.Tk()
root.geometry('750x100')
root.resizable(False, False)
root.title('github.com/hcm444')


# download button handler
def show_clicked():
    show()
    showinfo(
        title='Information',
        message='Show button clicked!'
    )


def generate_clicked():
    generate(1, 1, 1, 1, 1, 2)
    showinfo(
        title='Information',
        message='Generate button clicked!'
    )


def generate_all_clicked():
    generate_all()
    showinfo(
        title='Information',
        message='Generate All button clicked!'
    )


def generate_random_clicked():
    generate_random(1)
    showinfo(
        title='Information',
        message='Generate Random button clicked!'
    )


def clear_clicked():
    clear()
    showinfo(
        title='Information',
        message='Clear button clicked!'
    )


show_icon = tk.PhotoImage(file='assets/show.png')

generate_icon = tk.PhotoImage(file='./assets/generate.png')

generate_all_icon = tk.PhotoImage(file='./assets/generate_all.png')

generate_random_icon = tk.PhotoImage(file='./assets/generate_random.png')

clear_icon = tk.PhotoImage(file='assets/clear.png')

show_button = ttk.Button(
    root,
    image=show_icon,
    text='Show',
    compound=tk.LEFT,
    command=show_clicked
)

generate_button = ttk.Button(
    root,
    image=generate_icon,
    text='Generate',
    compound=tk.LEFT,
    command=generate_clicked
)

generate_all_button = ttk.Button(
    root,
    image=generate_all_icon,
    text='Generate All',
    compound=tk.LEFT,
    command=generate_all_clicked
)

generate_random_button = ttk.Button(
    root,
    image=generate_random_icon,
    text='Generate Random',
    compound=tk.LEFT,
    command=generate_random_clicked
)

clear_button = ttk.Button(
    root,
    image=clear_icon,
    text='Clear',
    compound=tk.LEFT,
    command=clear_clicked
)

show_button.pack(
    ipadx=5,
    ipady=5,
    expand=True,
    side=tk.LEFT,

)

generate_button.pack(
    ipadx=5,
    ipady=5,
    expand=True,
    side=tk.LEFT,
)

generate_all_button.pack(
    ipadx=5,
    ipady=5,
    expand=True,
    side=tk.LEFT,
)

generate_random_button.pack(
    ipadx=5,
    ipady=5,
    expand=True,
    side=tk.LEFT,
)

clear_button.pack(
    ipadx=5,
    ipady=5,
    expand=True,
    side=tk.LEFT,
)

root.mainloop()
