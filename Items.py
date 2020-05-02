import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt   

def GenrateGraph():
    Calculate()
    plt.style.use('ggplot')
    x = ['Income', 'Mortgague', 'Bills', 'Saving', 'Disposable']
    money = [int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), int(e1000.get())]
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos ,money ,  color='green')
    plt.xlabel("Expence")
    plt.ylabel("Money (£)")
    plt.title("where your money goes")
    plt.xticks(x_pos, x)
    plt.show()
    return

def Calculate():
    spent   = ( int(e2.get()) + int(e3.get()) + int(e4.get()) )
    income  = ( int(e1.get())   ) 
    total = income - spent   
    return  e1000.insert(0, total)

master = tk.Tk()
tk.Label(master, text="Income After Tax").grid(row=0)
tk.Label(master, text="Mortgage").grid(row=1)
''' 
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
'''
tk.Label(master, text="Bills").grid(row=2)
tk.Label(master, text="Saving?").grid(row=3)
tk.Label(master, text="Total;").grid(row=31, column = 0)




e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
'''
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)
e9 = tk.Entry(master)
e10 = tk.Entry(master)
'''

e1000 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

'''
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
e9.grid(row=8, column=1)
e10.grid(row=9, column=1)
'''
e1000.grid(row=31, column=1)


tk.Button(master, text='Quit', command=master.quit).grid(row=30, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Graph', command=GenrateGraph).grid(row=30, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Calculate', command=Calculate).grid(row=30, column=2, sticky=tk.W, pady=4)




tk.mainloop()