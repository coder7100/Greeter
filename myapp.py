import tkinter as tk

window = tk.Tk()

window.title("greeter")
# geometry is for setting the size of the window
window.geometry("400x400")

# --labels----

label1 = tk.Label(text="welcome to greeter ")
label1.grid(column=1, row=0)

label1 = tk.Label(text="Enter your name: ")
label1.grid(column=0, row=1)

# --entries----

entry1 = tk.Entry()
entry1.grid(column=1, row=1)

window.mainloop()
