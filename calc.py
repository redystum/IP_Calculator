from tkinter import *

root = Tk()

root.geometry("500x500")

root.resizable(0, 0)

root.title("Calcualtor")

def impt():
    if ipt.get().isdigit():
        binar()
    else:
        # iptt = Label(root, text="Digite apenas números!").pack()
        # ipt.delete(0, END)
        binar()

def binar():
    num = ipt.get().split(".")
    i = 0
    n = ["","","",""]
    for i in range(0, 4):
        num[i] = int(num[i])
        i = i + 1 

    i = 0
    for i in range(0, 4):
        n[i] = bin(num[i])[2:]
        i = i + 1

    iptt = Label(root, text=f"{n[0]}.{n[1]}.{n[2]}.{n[3]}").pack()
    

intro = Label(root, text="Introduza").pack()

ipt = Entry(root, width=60)
ipt.pack()


buton = Button(root, text="convert", command=impt).pack()


root.mainloop()