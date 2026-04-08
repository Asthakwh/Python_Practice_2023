import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My First GUI")
#root.geometry("300x200")  # Width x Height

# Add a label
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Run the GUI loop 
root.mainloop()
