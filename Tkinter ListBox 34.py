from tkinter import *
 
from tkinter import messagebox
 
window = Tk()
 
window.title("mrhuseyin.medium.com")
window.geometry("400x300")
 
#grid form çizdirme
application = Frame(window)
application.grid()
 
 
Lb1 = Listbox(application)
Lb1.insert(1, "Python")
Lb1.insert(2, "C#")
Lb1.insert(3, "JAVA")
Lb1.insert(4, "JAVASCRIPT")
Lb1.grid(padx=110, pady=10)
 
#draw form
window.mainloop()