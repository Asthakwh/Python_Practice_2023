from tkinter import *

# Function to handle button clicks
def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, END)
            entry.insert(END, result)
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif button_text == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, button_text)

# Main window
root = Tk()
root.title("Easy Calculator")

entry = Entry(root, width=25, font=('Arial', 20), bd=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for i in range(4):
    for j in range(4):
        btn = Button(root, text=buttons[i][j], padx=20, pady=20,
                     font=('Arial', 15), command=lambda text=buttons[i][j]: click(text))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()
