#!python3
import tkinter as tk

def do():
    x = entry1.get()
    y = entry2.get()
    label3["text"] = int(x) * int(y)

main = tk.Tk()

entry1 = tk.Entry(width = 25)
label1 = tk.Label(text = "x")
entry2 = tk.Entry(width = 25)
button1 = tk.Button(text = "=", command = do)
label3 = tk.Label(width = 40)

entry1.pack(side = "left")
label1.pack(side = "left")
entry2.pack(side = "left")
button1.pack(side = "left")
label3.pack(side = "left")

main.mainloop()