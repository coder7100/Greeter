import tkinter as tk
import random

window = tk.Tk()

window.title("greeter")
# geometry is for setting the size of the window
window.geometry("400x400")

# --functions----


def phrase_genrator():
    name = str(entry1.get())
    phrases = ["Hey", "Hello", "Ssup", "Have a Nice Day"]
    greeting = random.choice(phrases)+name
    # ---text field
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=1, row=3)
    greeting_display.insert(tk.END, greeting)

# --labels----


label1 = tk.Label(text="welcome to greeter ")
label1.grid(column=1, row=0)

label1 = tk.Label(text="Enter your name: ")
label1.grid(column=0, row=1)

# --entries----

entry1 = tk.Entry()
entry1.grid(column=1, row=1)

# --button

button1 = tk.Button(text="CLICK ME!", command=phrase_genrator)
button1.grid(column=1, row=2)

window.mainloop()
