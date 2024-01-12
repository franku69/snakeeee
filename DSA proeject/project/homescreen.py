import tkinter as tk
from main import setup_game, next_turn, change_direction, game_over

root = tk.Tk()
root.geometry('700x700')
root.title('Homescreen')
root.resizable(False, False)  # Make the window non-resizable

canvas = None
label = None
score = 0

def home_page():
    global canvas, label, score

    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame, text='Home Page\n\nPage: 1', font=('Bold', 30))
    lb.pack()

    # Set up the game on the canvas
    label = tk.Label(home_frame, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()

    home_frame.pack(padx=20)

def menu_page():
    menu_frame = tk.Frame(main_frame)
    lb = tk.Label(menu_frame, text='Menu Page\n\nPage: 2', font=('Bold', 30))
    lb.pack()
    menu_frame.pack(padx=20)

def groupmem_page():
    groupmem_frame = tk.Frame(main_frame)
    lb = tk.Label(groupmem_frame, text='Group Member Page\n\nPage: 3', font=('Bold', 30))
    lb.pack()
    groupmem_frame.pack(padx=20)

def hide_indicators():
    home_indicate.config(bg='#d1e0d5')
    menu_indicate.config(bg='#d1e0d5')
    groupmem_indicate.config(bg='#d1e0d5')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#030303')
    delete_pages()
    page()
    # Call setup_game() only when the "Home" button is clicked
    if lb == home_indicate:
        setup_game()

options_frame = tk.Frame(root, bg='#d1e0d5')

home_btn = tk.Button(options_frame, text='Home', font=('Bold', 15),
                     fg='#158aff', bd=0, bg='#d1e0d5',
                     command=lambda: indicate(home_indicate, home_page))
home_btn.place(x=10, y=50)

home_indicate = tk.Label(options_frame, text='', bg='#d1e0d5')
home_indicate.place(x=3, y=50, width=5, height=40)

menu_btn = tk.Button(options_frame, text='Menu', font=('Bold', 15),
                     fg='#158aff', bd=0, bg='#d1e0d5',
                     command=lambda: indicate(menu_indicate, menu_page))
menu_btn.place(x=10, y=100)

menu_indicate = tk.Label(options_frame, text='', bg='#d1e0d5')
menu_indicate.place(x=3, y=100, width=5, height=40)

groupmem_btn = tk.Button(options_frame, text='Members', font=('Bold', 15),
                         fg='#158aff', bd=0, bg='#d1e0d5',
                         command=lambda: indicate(groupmem_indicate, groupmem_page))
groupmem_btn.place(x=7, y=150)

groupmem_indicate = tk.Label(options_frame, text='', bg='#d1e0d5')
groupmem_indicate.place(x=3, y=150, width=5, height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=700)

main_frame = tk.Frame(root, highlightbackground='black',
                      highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=700, width=700)

root.mainloop()
