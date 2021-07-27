from tkinter import *
import re
from ipaddress import IPv4Address, IPv4Network

root = Tk()

root.geometry("500x500")

root.resizable(0, 0)

root.title("IP Calcualtor")

def validate():
    ip = ip_input.get()
    mask = mask_input.get()
    mask = int(mask)
    ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    if re.search(ip_regex, ip):
        if mask < 32 or mask > 1:
            screen_out()
        else:
            out = Label(root, text="Enter a valid Mask")
            out.place(x=250, y=80, anchor="center")
            mask_input.delete(0, END)
    else:
        if mask > 32 or mask < 1:
            out1 = Label(root, text="Enter a valid IP and Mask")
            out1.place(x=250, y=110, anchor="center")
            ip_input.delete(0, END)
            mask_input.delete(0, END)
        else:
            out2 = Label(root, text="Enter a valid IP")
            out2.place(x=250, y=100, anchor="center")
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

    # class_(n)
    return n


def class_ip(n):
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

    return ip_class


def Mask():
    algo = 2


def screen_out():
    n = binar()
    out = Label(root, text=f"IP Address:\t{ip_input.get()}  \t  {n[0]}.{n[1]}.{n[2]}.{n[3]}")
    out.place(x=250, y=120, anchor="center")
    # network
    out = Label(root, text="Network:\t")
    out.place(x=250, y=150, anchor="center")
    ip_class = class_ip(n)
    out = Label(root, text="Class: \t %s" % ip_class)
    out.place(x=250, y=180, anchor="center")
    # mask
    out = Label(root, text="Mask:\t")
    out.place(x=250, y=210, anchor="center")
    # broadcast
    out = Label(root, text="Broadcast:\t")
    out.place(x=250, y=240, anchor="center")
    # 1host
    out = Label(root, text="First on Host:\t")
    out.place(x=250, y=270, anchor="center")
    # last host
    out = Label(root, text="Last on Host:\t")
    out.place(x=250, y=300, anchor="center")
    # Hosts
    out = Label(root, text="Hostes:\t")
    out.place(x=250, y=330, anchor="center")

# Main

# Font for the displayed letters
font_title = ("Calibri", 20, "normal")
font_slash = ("Calibri", 15, "normal")

# Displayed title on window
title = Label(root, text="IP Calculator", font=font_title).place(
    x=250, y=20, anchor="center")

# Alignments to make the window more beauty
alignment = Label(root, text=" ").grid(row=0, column=0)
alignment = Label(root, text=" ").grid(row=1, column=0)
alignment = Label(root, text="        ").grid(row=2, column=0)

# Local to write your IP
ip_input = Entry(root, width=50)
ip_input.grid(row=2, column=1)

# Slash for separate IP to the Mask
slash = Label(root, text="/", font=font_slash).grid(row=2, column=3)

# Local to write your Mask
mask_input = Entry(root, width=20)
mask_input.grid(row=2, column=4)

# Button to convert
button = Button(root, text="Calculate", command=validate).place(
    x=250, y=90, anchor="center")

# For the window to always be updated
root.mainloop()
