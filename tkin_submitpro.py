from tkinter import *

def show_data():
    user = username_entry.get()
    pwd = password_entry.get()
    result.config(text="Username: " + user + "\nPassword: " + pwd)

# Create window
root = Tk()
root.title("Login Form")
#root.geometry("250x200")

# Username
Label(root, text="Username").pack()
username_entry = Entry(root)
username_entry.pack()

# Password
Label(root, text="Password").pack()
password_entry = Entry(root, show="*")
password_entry.pack()

# Submit button
Button(root, text="Submit", command=show_data).pack(pady=10)

# Output label
result = Label(root, text="")
result.pack()

root.mainloop()
