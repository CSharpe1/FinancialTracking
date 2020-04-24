import numpy as np
import matplotlib
import tkinter as tk


username = input("Enter username:")
password = input("Enter Password:")

date_month = input("Which Month is this for?")

total_spend = 0
total_left = 0

total_in = input("Enter Total income After tax:")
Mort = input("Enter Mortgague:")
Water = input("Enter water:")
Electricity = input("Enter Electricity:")
CouncilTax = input("Enter Council Tax:")
internet = input("Enter Internet:")
phone = input("Enter Phone:")
car_ins = input("Enter Car Insurance:")
home_ins = input("Enter Home insurance:")
travel = input("Enter Travel:")
TV = input("Enter TV:")
onlineTV = input("Enter Online TV, e.g. Netflix / Prime:")

total_spend = (Mort + Water + Electricity + CouncilTax + internet + phone + car_ins + home_ins + travel + TV + onlineTV)

total_left  = int(total_in) - int(total_spend)

print("Total spending:", total_spend)
print("Total Left Over:", (total_left))



window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.mainloop()