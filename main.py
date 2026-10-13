import tkinter as tk
from tkinter import Text


num = 1

def addlang():
    global num
    num += 1
    print("hi")
    print(num)

def remlang():
    global num
    if num <= 1:
        print("Cant be negative")
    else:
        num -= 1
        print("bye")
        print(num)

root = tk.Tk()
root.title("MultyTransL")
root.geometry("950x800")
root.configure(background="#82a2a2")
root.resizable(True, True)



label1 = tk.Label(root, text="Translator", background="#82a2a2", foreground="white", font=("Arial", 16))
label1.grid(row=0, column=1, pady=50, padx=50)

left = tk.Frame(root, background="#82a2a2")
left.grid(row=1, column=0, pady=50, padx=50)

transl1 = tk.Text(left, width=25, height=5)
transl1.grid(row=1, column=1, pady=10, padx=10)

cent = tk.Frame(root, background="#82a2a2")
cent.grid(row=1, column=1, pady=0, padx=0)

TBT = tk.Button(cent, text="Translate")
TBT.grid(row=0, column=1, pady=0, padx=0)


languages = {"German", "English", "Chinese (Simplified)", "Chinese (Traditional)"}

select1 = tk.StringVar()
select1.set("Pick")

dropdown1 = tk.OptionMenu(cent,select1, *languages)
dropdown1.grid(row=1, column=1, pady=50, padx=0)


right = tk.Frame(root, background="#82a2a2")
right.grid(row=1,column=2, pady=0, padx=20)

transr1 = tk.Text(right, width=25, height=5)
transr1.grid(row=1, column=1, pady=10, padx=10)

add = tk.Button(right, text="Add", command=lambda:addlang())
add.grid(row=2+num, column=1, pady=0, padx=0)

rem = tk.Button(right, text="Remove", command=lambda:remlang())
rem.grid(row=3+num, column=1, pady=10, padx=0)


root.minsize(450, 300)
root.mainloop()