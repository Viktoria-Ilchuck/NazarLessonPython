import tkinter as tk
import re

login_patter = re.compile(r"vika")
password_patter = re.compile(r"qw2/.g")




def login():
    login = login_entry.get()
    password = password_entry.get()


    if login_patter.search(login):
        if password_patter.search(password):
            login_entry.config(bg="green")

            password_entry.config(bg="green")

        else:
            login_entry.delete(0, tk.END)
            login_entry.config(bg="red")

            password_entry.delete(0, tk.END)
            password_entry.config(bg="red")

    else:
        login_entry.delete(0, tk.END)
        login_entry.config(bg="red")

        password_entry.delete(0, tk.END)
        password_entry.config(bg="red")



root = tk.Tk()
root.geometry("400x250+1000+500")
root.title("Login")
root.resizable(False,False)





login_label = tk.Label(root, text="Login",
                       font=("Arial",15),padx=50)


password_label = tk.Label(root, text="Password",
                       font=("Arial",15),padx=50)


login_entry = tk.Entry(root, font=("Arial",12),
                       width=20)


password_entry = tk.Entry(root, font=("Arial",12),
                       width=20,
                       show="*")


login_button = tk.Button(root, text="Login",
                         font=("Arial",16), width=15,
                         command=login)



root.grid_columnconfigure(0,minsize=150)
root.grid_columnconfigure(1,minsize=150)

root.grid_rowconfigure(0,minsize=90)
root.grid_rowconfigure(1,minsize=90)

login_button.grid(columnspan = 2)


login_label.grid(column=0, row=0)
password_label.grid(column=0, row=1)

login_entry.grid(column=1, row=0)
password_entry.grid(column=1, row=1)

login_button.grid(column=0, row=2)

root.mainloop()