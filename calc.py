from tkinter import *
import re
from ipaddress import IPv4Address, IPv4Network
import ipaddress

root = Tk()

root.geometry("500x500")

root.resizable(0, 0)

root.title("IP Calcualtor")

root.configure(bg='#2e2e2e')

# Validate if imput its a valid IP and Mask
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

# Binary IP
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

# Network
def network():
    ip = f"{ip_input.get()}/{int(mask_input.get())}"
    network_num = ipaddress.ip_network(ip, strict=False)
    return network_num

# Network
def network_bin(network_num):
    network_num = str(network_num)
    net = network_num.split("/")
    network = net[0].split(".")
    i = 0
    n = ["", "", "", ""]    
    for i in range(0, 4):
        n[i] = bin(int(network[i]))[2:]
        i = i + 1

    network_binar = f"{n[0]}.{n[1]}.{n[2]}.{n[3]}"
    return network_binar

# Mask
def Mask():
    i = 0
    netmask_bin = StringVar()
    num_mask_string = StringVar()
    num_mask = ["0","0","0","0","0","0","0","0",".","0","0","0","0","0","0","0","0",".","0","0","0","0","0","0","0","0",".","0","0","0","0","0","0","0","0"]
    one_number = int(mask_input.get())
    if one_number > 24 :
        one_number = one_number + 3
    elif one_number > 16 :
        one_number = one_number + 2
    elif one_number > 8 :
        one_number = one_number + 1
    for i in range(0, one_number):
        if (i == 8 or i == 17 or i == 26):
            num_mask[i] = "."
        else:
            num_mask[i] = "1"
        i = i + 1
    netmask_bin = str(num_mask)
    netmask_bin = netmask_bin.replace(" ","").replace("'","").replace(",","").replace("[","").replace("]","")
    return netmask_bin

# Mask
def mask_bin_covertion(netmask_bin):
    num = netmask_bin.split(".")
    i = 0
    n = ["", "", "", ""]
    i = i + 1
    for i in range(0, 4):
        n[i] = int(num[i], 2)
        i = i + 1
    netmask = f"{n[0]}.{n[1]}.{n[2]}.{n[3]}"
    return netmask

# Class
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

# Broadcast
def broadcast_calc():
    ip = f"{ip_input.get()}/{int(mask_input.get())}"
    net = ipaddress.IPv4Network(ip, False )
    broadcast = net.broadcast_address
    return broadcast

# Broadcast
def broadcast_bin(broadcast):
    broadcast = str(broadcast)
    num = broadcast.split(".")
    i = 0
    n = ["", "", "", ""]
    i = i + 1
    for i in range(0, 4):
        n[i] = bin(int(num[i]))[2:]
        i = i + 1
    broadcast_binar = f"{n[0]}.{n[1]}.{n[2]}.{n[3]}"
    return broadcast_binar

# First Host
def fist_host(network_num):
    network_num = str(network_num)
    network_num = network_num.split("/")
    network_num = network_num[0].split(".")
    if network_num[3] == "255":
        first = network_num
    else:
        network_num[3] = int(network_num[3])
        network_num[3] = network_num[3] + 1
        first = network_num
    first = str(first)
    first = first.replace(" ","").replace("'","").replace(",",".").replace("[","").replace("]","")
    return first

# First on Host
def first_bin(first):
    num = first.split(".")
    i = 0
    n = ["", "", "", ""]
    i = i + 1
    for i in range(0, 4):
        n[i] = bin(int(num[i]))[2:]
        i = i + 1
    first_binar = f"{n[0]}.{n[1]}.{n[2]}.{n[3]}"
    return first_binar

# Last on Host
def last_host(broadcast):
    broadcast = str(broadcast)
    broadcast = broadcast.split("/")
    broadcast = broadcast[0].split(".")
    broadcast[3] = int(broadcast[3])
    broadcast[3] = broadcast[3] - 1 # THIS LINE DONT WORK, IDK WHY
    last = broadcast
    last = str(last)
    last = last.replace(" ","").replace("'","").replace(",",".").replace("[","").replace("]","")
    return last

# Last on Host
def last_bin(last):
    num = last.split(".")
    i = 0
    n = ["", "", "", ""]
    i = i + 1
    for i in range(0, 4):
        n[i] = bin(int(num[i]))[2:]
        i = i + 1
    last_binar = f"{n[0]}.{n[1]}.{n[2]}.{n[3]}"
    return last_binar


# Hosts
def hosts_number():
    mask = int(mask_input.get())
    if mask == 32:
        hosts = 1
    else:
        zero_number = 32 - mask
        hosts = (2**zero_number)-2
    return hosts

# Display results
def screen_out():
    # Binary IP
    ip_binar = binar()
    ip_out.set(ip_input.get())
    ip_binary_out.set(ip_binar)

    # Network
    network_num = network()
    network_out.set(network_num)
    network_binar = network_bin(network_num)
    network_binary_out.set(network_binar)

    # Mask
    netmask_bin = Mask()
    mask_binary_out.set(netmask_bin)
    netmask = mask_bin_covertion(netmask_bin)
    mask_out.set(netmask)

    # class
    ip_class = class_ip(ip_binar)
    class_out.set(ip_class)

    # Broadcast
    broadcast = broadcast_calc()
    broadcast_out.set(broadcast)
    broadcast_binar = broadcast_bin(broadcast)
    broadcast_binary_out.set(broadcast_binar)

    # First on Host
    first = fist_host(network_num)
    first_out.set(first)
    first_binar = first_bin(first)
    first_binary_out.set(first_binar)

    # last on host
    last = fist_host(broadcast)
    last_out.set(last)
    last_binar = first_bin(last)
    last_binary_out.set(last_binar)

    # Hosts
    hosts = hosts_number()
    hosts_out.set(hosts)

# Main

# Font for the displayed letters
font_title = ("Calibri", 20, "normal")
font_slash = ("Calibri", 15, "normal")

# Displayed title on window
title = Label(root, text="IP Calculator", font=font_title, bg='#2e2e2e', fg="white").place(x=250, y=20, anchor="center")

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
