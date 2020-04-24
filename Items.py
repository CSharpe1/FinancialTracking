import numpy as np
import matplotlib
import tkinter as tk


# username = input("Enter username:")
# password = input("Enter Password:")

# date_month = input("Which Month is this for?")

# total_spend = 0
# total_left = 0

# total_in = input("Enter Total income After tax:")
# Mort = input("Enter Mortgague:")
# Water = input("Enter water:")
# Electricity = input("Enter Electricity:")
# CouncilTax = input("Enter Council Tax:")
# internet = input("Enter Internet:")
# phone = input("Enter Phone:")
# car_ins = input("Enter Car Insurance:")
# home_ins = input("Enter Home insurance:")
# travel = input("Enter Travel:")
# TV = input("Enter TV:")
# onlineTV = input("Enter Online TV, e.g. Netflix / Prime:")

# total_spend = (Mort + Water + Electricity + CouncilTax + internet + phone + car_ins + home_ins + travel + TV + onlineTV)

# total_left  = int(total_in) - int(total_spend)

# print("Total spending:", total_spend)
# print("Total Left Over:", (total_left))

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))


def Calculate():
    allitems =  (e2.get() + e3.get() + e4.get() + e5.get() + e6.get() + e7.get() + e8.get() + e9.get() + e10.get())
    b = sum(int(allitems))
    print("Total Spent: %s" % allitems          )#    (e2.get() + e3.get() + e4.get() + e5.get() + e6.get() + e7.get() + e8.get() + e9.get() + e10.get()  ))



master = tk.Tk()
tk.Label(master, text="Income After Tax").grid(row=0)
tk.Label(master, text="Mortgage").grid(row=1)
tk.Label(master, text="House service charge").grid(row=2)
tk.Label(master, text="Internet/TV/Home phone bundle").grid(row=3)
tk.Label(master, text="Mobile").grid(row=4)
tk.Label(master, text="Water").grid(row=5)
tk.Label(master, text="Home Insurance").grid(row=6)
tk.Label(master, text="Car insurance").grid(row=7)
tk.Label(master, text="Dept payments inc. credit card fees").grid(row=8)
tk.Label(master, text="Saving?").grid(row=9)
tk.Label(master, text="One off expense;").grid(row=10, column = 0)
tk.Label(master, text="Details;").grid(row=10, column = 1)

tk.Label(master, text="Total;").grid(row=31, column = 0)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)
e9 = tk.Entry(master)
e10 = tk.Entry(master)


e1000 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
e9.grid(row=8, column=1)
e10.grid(row=9, column=1)

e1000.grid(row=31, column=1)


tk.Button(master, text='Quit', command=master.quit).grid(row=30, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=30, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Calculate', command=Calculate).grid(row=30, column=2, sticky=tk.W, pady=4)




tk.mainloop()