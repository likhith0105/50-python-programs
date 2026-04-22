from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("mrhuseyin.medium.com")
window.geometry("400x300")
#plotting grid forms
application = Frame(window)
application.grid()
L1 = Label(application, text="Enter your name")
L1.grid(padx=110, pady=10)
E1 = Entry(application, bd =2)
E1.grid(padx=110, pady=3)
#draw form
window.mainloop()