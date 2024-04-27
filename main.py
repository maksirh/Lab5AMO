import tkinter as tk
import functions
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Головне вікно")


# windows
def option():
    root2 = tk.Toplevel(root)
    im1 = Image.open("variant.png")
    image1 = ImageTk.PhotoImage(im1)

    root2.title("Завдання до варіанту")

    label1 = tk.Label(root2, image=image1)
    label1.grid()
    root2.mainloop()


def matrixKoef():
    root3 = tk.Toplevel(root)
    root3.mainloop()


# labels

lab1 = tk.Label(text='Лабораторна робота №5', font=("Times New Roman", 15))

# main buttons
but1 = tk.Button(text='Ввести коефіціенти матриці', font=("Times New Roman", 12), command=matrixKoef)
but2 = tk.Button(text='Завдання за варіантом', font=("Times New Roman", 12), command=option)

# grid
lab1.grid(row=0, column=0, sticky='wens')
but1.grid(row=2, column=0, sticky='wens')
but2.grid(row=1, column=0, sticky='wens')

# root

root.grid_rowconfigure(0, minsize=50)
root.grid_rowconfigure(1, minsize=50)
root.grid_rowconfigure(2, minsize=50)
root.grid_columnconfigure(0, minsize=500)
root.geometry("500x500")
root.mainloop()
