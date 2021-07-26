from tkinter import *
import re
from ipaddress import IPv4Address, IPv4Network

root = Tk()

root.geometry("500x500")

root.resizable(0, 0)

root.title("IP Calcualtor")


def validate():
    ip = ip_input.get()
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    if (re.search(regex, ip)):
        binar()
    else:
        iptt = Label(root, text="Enter a valid IP ").pack()
        ip_input.delete(0, END)

def binar():
    num = ip_input.get().split(".")
    i = 0
    n = ["", "", "", ""]
    for i in range(0, 4):
        num[i] = int(num[i])
        i = i + 1

    i = 0
    for i in range(0, 4):
        n[i] = bin(num[i])[2:]
        i = i + 1

    iptt = Label(root, text=f"{n[0]}.{n[1]}.{n[2]}.{n[3]}").pack()
    class_(n)


def class_(n):
    classA = IPv4Network(("10.0.0.0", "255.0.0.0"))
    classB = IPv4Network(("172.16.0.0", "255.240.0.0"))
    classC = IPv4Network(("192.168.0.0", "255.255.0.0"))

    ip = IPv4Address(ip_input.get())

    if ip in classA:
        ip_class = "A - Private"
    elif ip in classB:
        ip_class = "B - Private"
    elif ip in classC:
        ip_class = "C - Private"
    elif n[0].startswith('0'):
        ip_class = "A - Public"
    elif n[0].startswith('10'):
        ip_class = "B - Public"
    elif n[0].startswith('110'):
        ip_class = "C - Public"
    elif n[0].startswith('1110'):
        ip_class = "D - Public"
    else:
        ip_class = "E - Public"

    out = Label(root, text="Class: %s" % ip_class).pack()


#iptt = Label(root, text=f"{n[0]}.{n[1]}.{n[2]}.{n[3]}").pack()
intro = Label(root, text="IP Calculator").pack()

ip_input = Entry(root, width=60)
ip_input.pack()

buton = Button(root, text="Calculate", command=validate).pack()



root.mainloop()
