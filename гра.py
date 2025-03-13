import tkinter as tk

def check_number():

    pass

def new_game():

    pass


root = tk.Tk()
root.geometry("400x400")
root.title("Вгадай число")
root.resizable(False, False)

title_label = tk.Label(root, text="Вгадай число", font=("Arial", 20), pady=10)


hint_label = tk.Label(root, text="Введіть число від 1 до 100", font=("Arial", 14), pady=10)


number_entry = tk.Entry(root, font=("Arial", 14), width=10, justify="center")

check_button = tk.Button(root, text="Перевірити", font=("Arial", 14), width=15, command=check_number)


result_label = tk.Label(root, text="", font=("Arial", 14), pady=10)

new_game_button = tk.Button(root, text="Нова гра", font=("Arial", 14), width=15, command=new_game)


root.grid_columnconfigure(0, weight=1)
title_label.grid(column=0, row=0, pady=10)
hint_label.grid(column=0, row=1)
number_entry.grid(column=0, row=2, pady=10)
check_button.grid(column=0, row=3, pady=10)
result_label.grid(column=0, row=4)
new_game_button.grid(column=0, row=5, pady=10)


root.mainloop()