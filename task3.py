#!python3
import tkinter as tk
from tkinter import *

main = tk.Tk()
main.geometry("256x200")
main.title("DOGECOIN")
main.resizable(0, 0)

dogphoto = PhotoImage(file = "dog.png")
label1 = tk.Label(main, image = dogphoto,)
label2 = tk.Label(text = "Pochacco!")
label3 = tk.Label(bg = "cyan", text = "A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero")

label1.place(x = 80, y = 20)
label2.place(x = 150, y = 60)
label3.place(x = 0,y = 165)

main.mainloop()