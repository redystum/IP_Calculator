from tkinter import *
import re
from ipaddress import IPv4Address, IPv4Network

root = Tk()

root.geometry("500x500")

root.resizable(0, 0)

root.title("IP Calcualtor")

root.configure(bg='#2e2e2e')

def validate():
    ip = ip_input.get()
    mask = mask_input.get()
    ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    try:
        mask = int(mask)
    except ValueError:
        if (re.search(ip_regex, ip)) == None:
            validate_var.set("Enter a valid IP and Mask")
            ip_input.delete(0, END)
            mask_input.delete(0, END)
        else:
            validate_var.set("Enter a valid Mask")
            mask_input.delete(0, END)
        
    mask = int(mask)

    if re.search(ip_regex, ip):
        if mask > 32 or mask < 1:
            validate_var.set("Enter a valid Mask")
            mask_input.delete(0, END)
        else:
            screen_out()
    else:
        if mask > 32 or mask < 1:
            validate_var.set("Enter a valid IP and Mask")
            ip_input.delete(0, END)
            mask_input.delete(0, END)
        else:
            validate_var.set("Enter a valid IP")
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

    ip_binar = f"{n[0]}.{n[1]}.{n[2]}.{n[3]}"
    return ip_binar


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
    i = 0
    netmask_bin = StringVar()
    num_mask_string = StringVar()
    num_mask = ["0","0","0","0","0","0","0","0",".","0","0","0","0","0","0","0","0",".","0","0","0","0","0","0","0","0",".","0","0","0","0","0","0","0","0"]
    one_number = int(mask_input.get())
    for i in range(0, one_number):
        if (i == 8 or i == 16 or i == 24):
            num_mask[i] = "."
        else:
            num_mask[i] = "1"
        i = i + 1
    netmask_bin = str(num_mask)
    return netmask_bin

def mask_bin_covertion(netmask_bin):
    num = netmask_bin.split(".")
    i = 0
    n = ["", "", "", ""]
    i = i + 1
    i = 0
    for i in range(0, 4):
        n[i] = int(num[i], 2)
        i = i + 1
    netmask = f"{n[0]}.{n[1]}.{n[2]}.{n[3]}"
    return netmask





def screen_out():
    # Binary IP
    ip_binar = binar()
    ip_out.set(ip_input.get())
    ip_binary_out.set(ip_binar)
    # network
    
    # mask
    netmask_bin = Mask()
    netmask_bin = netmask_bin.replace(" ","").replace("'","").replace(",","").replace("[","").replace("]","")
    mask_binary_out.set(netmask_bin)
    netmask = mask_bin_covertion(netmask_bin)
    mask_out.set(netmask)
    # class
    ip_class = class_ip(ip_binar)
    class_out.set(ip_class)
    # broadcast

    # 1host

    # last host

    # Hosts

    1+1


# Main

# Font for the displayed letters
font_title = ("Calibri", 20, "normal")
font_slash = ("Calibri", 15, "normal")

# Displayed title on window
title = Label(root, text="IP Calculator", font=font_title, bg='#2e2e2e', fg="white").place(
    x=250, y=20, anchor="center")

# Alignments to make the window more beauty
alignment = Label(root, text=" ", bg='#2e2e2e').grid(row=0, column=0)
alignment = Label(root, text=" ", bg='#2e2e2e').grid(row=1, column=0)
alignment = Label(root, text="        ", bg='#2e2e2e').grid(row=2, column=0)

# Local to write your IP
ip_input = Entry(root, width=50, bg='#0f0f0f', fg="white")
ip_input.grid(row=2, column=1)

# Slash for separate IP to the Mask
slash = Label(root, text="/", font=font_slash, bg='#2e2e2e', fg="white").grid(row=2, column=3)

validate_var = StringVar()

validate_var.set("Enter an IP and Mask")
# Local to write your Mask
mask_input = Entry(root, width=20, bg='#0f0f0f', fg="white")
mask_input.grid(row=2, column=4)

out = Entry(root, textvariable=validate_var, width=30, justify = CENTER, bg='#2e2e2e', fg="white", bd="0")
out.place(x=250, y=81, anchor="center")

# Button to convert
button = Button(root, text="Calculate", command=validate, bg='#0f0f0f', fg="white").place(x=250, y=120, anchor="center")

# GUI

# Binary ip
ip_out  = StringVar()
ip_binary_out  = StringVar()

out = Label(root, text=f"IP Address:", bg='#2e2e2e', fg="white")
out.place(x=55, y=160, anchor="center")

out = Entry(root, textvariable=ip_out, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=170, y=160, anchor="center")
out = Entry(root, textvariable=ip_binary_out, width=35, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=370, y=160, anchor="center")

# Network
network_out = StringVar()
network_binary_out = StringVar()

out = Label(root, text="Network:", bg='#2e2e2e', fg="white")
out.place(x=55, y=200, anchor="center")

out = Entry(root, textvariable=network_out, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=170, y=200, anchor="center")
out = Entry(root, textvariable=network_binary_out, width=35, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=370, y=200, anchor="center")

# Class
class_out = StringVar()

out = Label(root, text="Class:", bg='#2e2e2e', fg="white")
out.place(x=55, y=240, anchor="center")

out = Entry(root, textvariable=class_out, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=170, y=240, anchor="center")

# Mask
mask_out = StringVar()
mask_binary_out = StringVar()

out = Label(root, text="Mask:", bg='#2e2e2e', fg="white")
out.place(x=55, y=280, anchor="center")

out = Entry(root, textvariable=mask_out, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=170, y=280, anchor="center")
out = Entry(root, textvariable=mask_binary_out, width=35, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=370, y=280, anchor="center")

# Broadcast
broadcast_out = StringVar()
broadcast_binary_out = StringVar()

out = Label(root, text="Broadcast:", bg='#2e2e2e', fg="white")
out.place(x=55, y=320, anchor="center")

out = Entry(root, textvariable=broadcast_out, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=170, y=320, anchor="center")
out = Entry(root, textvariable=broadcast_binary_out, width=35, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=370, y=320, anchor="center")

# First host
first_out = StringVar()
first_binary_out = StringVar()

out = Label(root, text="First on Host:", bg='#2e2e2e', fg="white")
out.place(x=55, y=360, anchor="center")

out = Entry(root, textvariable=first_out, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=170, y=360, anchor="center")
out = Entry(root, textvariable=first_binary_out, width=35, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=370, y=360, anchor="center")

# Last host
last_out = StringVar()
last_binary_out = StringVar()

out = Label(root, text="Last on Host:", bg='#2e2e2e', fg="white")
out.place(x=55, y=400, anchor="center")

out = Entry(root, textvariable=last_out, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=170, y=400, anchor="center")
out = Entry(root, textvariable=last_binary_out, width=35, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=370, y=400, anchor="center")

# Hosts
hosts_out = StringVar()

out = Label(root, text="Hostes:", bg='#2e2e2e', fg="white")
out.place(x=55, y=440, anchor="center")

out = Entry(root, textvariable=hosts_out, justify = CENTER, bg='#0f0f0f', fg="white")
out.place(x=170, y=440, anchor="center")

# For the window to always be updated
root.mainloop()
