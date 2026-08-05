from tkinter import *

window=Tk()

colors=["green", "red", "orange", "white", "yellow", "blue"]

for i, c in enumerate(colors):
    label=Label(window, text=c)
    label.grid(row=i, column=0, pady=5)

    button=Button(window, bg=c)
    button.grid(row=i, column=1)




window.mainloop()