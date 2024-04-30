import tkinter as tk
import functions
from tkinter import messagebox
from PIL import ImageTk, Image
import copy

xlist = []
diagonal = []
listRozv = []
listRozv2 = []
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
    def perev():

        global sumlist
        sumlist = []
        global sumkoef
        sumkoef = []
        longv = len(listViln)
        global c
        c = 0
        t = 0
        for i in range(longv):
            diagonal.append(listKoef[i * (longv + 1)])
            sumlist = []
            for i3 in range(longv):
                sumlist.append(listKoef[i3 + t])
            sumkoef.append(sum(sumlist))
            t += longv

        for i2 in range(longv):
            if 2 * diagonal[i2] < sumkoef[i2]:
                messagebox.showinfo('Перевірка', 'Помилка, метод Якобі росходиться')
                c += 1
                break
        if c == 0:
            messagebox.showinfo('Перевірка', 'Метод Якобі сходиться')

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
        for k2 in range(1, len(listViln)+1):
            xlist.append(f'x{k2}')



    root3 = tk.Toplevel(root)
    lab31 = tk.Label(root3, text='Введіть коефіціенти СЛАР:', font=("Times New Roman", 15))
    ent31 = tk.Entry(root3)
    but31 = tk.Button(root3, text='Зчитати коефіціенти матриці', font=("Times New Roman", 15), command=zchitKoef)
    lab32 = tk.Label(root3, text='Введіть вектор вільних коефіціентів:', font=("Times New Roman", 15))
    ent32 = tk.Entry(root3)
    but32 = tk.Button(root3, text='Зчитати вектор вільних коефіціентів', font=("Times New Roman", 15),
                      command=zchitViln)
    but33 = tk.Button(root3, text='Перевірити чи сходиться метод Якобі', font=("Times New Roman", 15), command=perev)
    ent31.grid(row=1, column=0, sticky='wens')
    lab31.grid(row=0, column=0, sticky='wens')
    but31.grid(row=2, column=0, sticky='wens')
    ent32.grid(row=4, column=0, sticky='wens')
    lab32.grid(row=3, column=0, sticky='wens')
    but32.grid(row=5, column=0, sticky='wens')
    but33.grid(row=6, column=0, sticky='wens')
    root3.grid_rowconfigure(0, minsize=50)
    root3.grid_rowconfigure(1, minsize=30)
    root3.grid_rowconfigure(2, minsize=50)
    root3.grid_rowconfigure(3, minsize=50)
    root3.grid_rowconfigure(4, minsize=30)
    root3.grid_rowconfigure(5, minsize=50)
    root3.grid_columnconfigure(0, minsize=300)
    root3.grid_columnconfigure(1, minsize=300)
    root3.geometry("345x320")
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
    listRozv = [0]*len(listViln)
    newlistkoef = copy.deepcopy(listKoef)


    for i4 in range(len(listViln)):
        newlistkoef[i4 * (len(listViln) + 1)] = 0

    for k in range(1000):
        t2 = 0
        list2 = []
        listRozv2 = []
        for i5 in range(len(listViln)):
            list1 = []
            for i6 in range(len(listViln)):
                list1.append(listRozv[i6] * newlistkoef[i6 + t2])
            list2.append(sum(list1))
            t2 += len(listViln)

        for i7 in range(len(listViln)):
            listRozv2.append(-1 / diagonal[i7] * (list2[i7] - listViln[i7]))

        listRozv = copy.deepcopy(listRozv2)

    kor = ''
    for roz in range(len(xlist)):
        kor += f'{xlist[roz]} = {listRozv[roz]}\n'

    messagebox.showinfo("Розв'язок СЛАР", kor)


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
root.geometry("500x250")
root.mainloop()
