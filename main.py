import tkinter as tk
import functions
from PIL import ImageTk, Image

listKoef = []
listViln = []
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
    def zchitKoef():
        global listKoef
        listKoef = []
        for koef in ent31.get().split(','):
            listKoef.append(int(koef))

    def zchitViln():
        global listViln
        listViln = []
        for viln in ent32.get().split(','):
            listViln.append(int(viln))

    root3 = tk.Toplevel(root)
    lab31 = tk.Label(root3, text='Введіть коефіціенти СЛАР:', font=("Times New Roman", 15))
    ent31 = tk.Entry(root3)
    but31 = tk.Button(root3, text='Зчитати коефіціенти матриці', font=("Times New Roman", 15), command=zchitKoef)
    lab32 = tk.Label(root3, text='Введіть вектор вільних коефіціентів:', font=("Times New Roman", 15))
    ent32 = tk.Entry(root3)
    but32 = tk.Button(root3, text='Зчитати вектор вільних коефіціентів', font=("Times New Roman", 15),
                      command=zchitViln)
    ent31.grid(row=1, column=0, sticky='wens')
    lab31.grid(row=0, column=0, sticky='wens')
    but31.grid(row=2, column=0, sticky='wens')
    ent32.grid(row=4, column=0, sticky='wens')
    lab32.grid(row=3, column=0, sticky='wens')
    but32.grid(row=5, column=0, sticky='wens')
    root3.grid_rowconfigure(0, minsize=50)
    root3.grid_rowconfigure(1, minsize=30)
    root3.grid_rowconfigure(2, minsize=50)
    root3.grid_rowconfigure(3, minsize=50)
    root3.grid_rowconfigure(4, minsize=30)
    root3.grid_rowconfigure(5, minsize=50)
    root3.grid_columnconfigure(0, minsize=300)
    root3.grid_columnconfigure(1, minsize=300)
    root3.geometry("345x270")
    root3.wait_window()


def slar():
    root4 = tk.Toplevel(root)
    lab41 = tk.Label(root4, text=functions.funcslar(listKoef, listViln), font=("Arial", 20))
    lab41.grid(row=0, column=0, sticky='wens')
    root4.title('СЛАР')
    root4.grid_rowconfigure(0, minsize=50)
    root4.geometry("500x400")
    root4.wait_window()


def rozv():
    koren = []
    for i in range(len(listViln)):
        koren.append(0)
    for i1 in range(len(listKoef)):
        a = listKoef[i1 * (len(listViln) + i1)]


# labels

lab1 = tk.Label(text='Лабораторна робота №5', font=("Times New Roman", 15))

# main buttons
but1 = tk.Button(text='Ввести коефіціенти матриці', font=("Times New Roman", 12), command=matrixKoef)
but2 = tk.Button(text='Завдання за варіантом', font=("Times New Roman", 12), command=option)
but3 = tk.Button(text='Подивитись вид СЛАР', font=("Times New Roman", 12), command=slar)
but4 = tk.Button(text="Розв'язок СЛАР", font=("Times New Roman", 12), command=rozv)

# grid
lab1.grid(row=0, column=0, sticky='wens')
but1.grid(row=2, column=0, sticky='wens')
but2.grid(row=1, column=0, sticky='wens')
but3.grid(row=3, column=0, sticky='wens')
but4.grid(row=4, column=0, sticky='wens')

# root

root.grid_rowconfigure(0, minsize=50)
root.grid_rowconfigure(1, minsize=50)
root.grid_rowconfigure(2, minsize=50)
root.grid_rowconfigure(3, minsize=50)
root.grid_rowconfigure(4, minsize=50)
root.grid_columnconfigure(0, minsize=500)
root.geometry("500x500")
root.mainloop()