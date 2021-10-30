from tkinter import *
import tkinter

def nwdo():
    nw = Tk()
    nw.title("Todo")
    nw.geometry("300x300")

    lb = Label(nw, text="     TO DO LIST          ").grid(row=0, column=1)
    lbl = Label(nw, text="Enter your task    ").grid(row=1, column=0)
    en = Entry(nw, width = 30, borderwidth = 5)
    en.grid(row=1, column=1)
    en1 = Entry(nw, width = 30, borderwidth = 5)
    en1.grid(row=2, column=1)
    lbl1 = Label(nw, text="Enter Time   ").grid(row=2, column=0)

    def submit():
        en.delete(0, END)
        en1.delete(0, END)



    btn_submit = Button(nw, text="Submit", command=submit).grid(row=3, column=1)


root = Tk()
root.title("Calender")
root.geometry("1500x750")

# label for January:-
lab = Label(root, text="January").grid(row=0, column=0, columnspan=7)

lb = Label(root, text="Mon").grid(row=1, column=0)
lb = Label(root, text="Tue").grid(row=1, column=1)
lb = Label(root, text="Wed").grid(row=1, column=2)
lb = Label(root, text="Thu").grid(row=1, column=3)
lb = Label(root, text="Fri").grid(row=1, column=4)
lb = Label(root, text="Sat").grid(row=1, column=5)
lb = Label(root, text="Sun").grid(row=1, column=6)

# Buttons for January:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=2, column=2)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=2, column=3)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=2, column=4)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=2, column=5)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=2, column=6)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=3, column=0)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=3, column=1)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=3, column=2)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=3, column=3)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=3, column=4)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=3, column=5)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=3, column=6)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=4, column=0)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=4, column=1)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=4, column=2)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=4, column=3)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=4, column=4)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=4, column=5)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=4, column=6)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=5, column=0)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=5, column=1)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=5, column=2)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=5, column=3)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=5, column=4)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=5, column=5)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=5, column=6)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=6, column=0)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=6, column=1)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=6, column=2)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=6, column=3)

btn31 = Button(root, text="31", padx=12, pady=10, command=nwdo).grid(row=6, column=4)

label = Label(root, text="             ").grid(row=4, column=8)

# label for Fabruary:-
lab = Label(root, text="Fabruary").grid(row=0, column=11, columnspan=7)

lb = Label(root, text="Mon").grid(row=1, column=10)
lb = Label(root, text="Tue").grid(row=1, column=11)
lb = Label(root, text="Wed").grid(row=1, column=12)
lb = Label(root, text="Thu").grid(row=1, column=13)
lb = Label(root, text="Fri").grid(row=1, column=14)
lb = Label(root, text="Sat").grid(row=1, column=15)
lb = Label(root, text="Sun").grid(row=1, column=16)

# Buttons for Fabruary:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=2, column=15)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=2, column=16)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=3, column=10)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=3, column=11)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=3, column=12)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=3, column=13)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=3, column=14)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=3, column=15)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=3, column=16)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=4, column=10)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=4, column=11)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=4, column=12)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=4, column=13)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=4, column=14)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=4, column=15)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=4, column=16)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=5, column=10)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=5, column=11)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=5, column=12)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=5, column=13)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=5, column=14)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=5, column=15)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=5, column=16)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=6, column=10)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=6, column=11)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=6, column=12)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=6, column=13)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=6, column=14)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=6, column=15)

label = Label(root, text="             ").grid(row=4, column=18)

# label for March:-
lab = Label(root, text="March").grid(row=0, column=20, columnspan=7)

lb = Label(root, text="Mon").grid(row=1, column=20)
lb = Label(root, text="Tue").grid(row=1, column=21)
lb = Label(root, text="Wed").grid(row=1, column=22)
lb = Label(root, text="Thu").grid(row=1, column=23)
lb = Label(root, text="Fri").grid(row=1, column=24)
lb = Label(root, text="Sat").grid(row=1, column=25)
lb = Label(root, text="Sun").grid(row=1, column=26)

# Buttons for March:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=2, column=26)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=3, column=20)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=3, column=21)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=3, column=22)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=3, column=23)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=3, column=24)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=3, column=25)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=3, column=26)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=4, column=20)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=4, column=21)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=4, column=22)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=4, column=23)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=4, column=24)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=4, column=25)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=4, column=26)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=5, column=20)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=5, column=21)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=5, column=22)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=5, column=23)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=5, column=24)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=5, column=25)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=5, column=26)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=6, column=20)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=6, column=21)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=6, column=22)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=6, column=23)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=6, column=24)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=6, column=25)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=6, column=26)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=2, column=20)

btn31 = Button(root, text="31", padx=12, pady=10, command=nwdo).grid(row=2, column=21)

label = Label(root, text="             ").grid(row=4, column=28)

# label for April:-
lab = Label(root, text="April").grid(row=0, column=30, columnspan=7)

lb = Label(root, text="Mon").grid(row=1, column=30)
lb = Label(root, text="Tue").grid(row=1, column=31)
lb = Label(root, text="Wed").grid(row=1, column=32)
lb = Label(root, text="Thu").grid(row=1, column=33)
lb = Label(root, text="Fri").grid(row=1, column=34)
lb = Label(root, text="Sat").grid(row=1, column=35)
lb = Label(root, text="Sun").grid(row=1, column=36)

# Buttons for April:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=2, column=32)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=2, column=33)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=2, column=34)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=2, column=35)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=2, column=36)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=3, column=30)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=3, column=31)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=3, column=32)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=3, column=33)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=3, column=34)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=3, column=35)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=3, column=36)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=4, column=30)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=4, column=31)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=4, column=32)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=4, column=33)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=4, column=34)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=4, column=35)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=4, column=36)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=5, column=30)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=5, column=31)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=5, column=32)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=5, column=33)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=5, column=34)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=5, column=35)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=5, column=36)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=6, column=30)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=6, column=31)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=6, column=32)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=6, column=33)

# label for May:-
lab = Label(root, text="May").grid(row=10, column=0, columnspan=7)

lb = Label(root, text="Mon").grid(row=11, column=0)
lb = Label(root, text="Tue").grid(row=11, column=1)
lb = Label(root, text="Wed").grid(row=11, column=2)
lb = Label(root, text="Thu").grid(row=11, column=3)
lb = Label(root, text="Fri").grid(row=11, column=4)
lb = Label(root, text="Sat").grid(row=11, column=5)
lb = Label(root, text="Sun").grid(row=11, column=6)

# Buttons for May:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=12, column=4)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=12, column=5)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=12, column=6)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=13, column=0)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=13, column=1)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=13, column=2)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=13, column=3)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=13, column=4)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=13, column=5)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=13, column=6)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=14, column=0)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=14, column=1)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=14, column=2)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=14, column=3)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=14, column=4)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=14, column=5)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=14, column=6)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=15, column=0)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=15, column=1)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=15, column=2)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=15, column=3)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=15, column=4)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=15, column=5)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=15, column=6)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=16, column=0)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=16, column=1)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=16, column=2)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=16, column=3)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=16, column=4)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=16, column=5)

btn31 = Button(root, text="31", padx=12, pady=10, command=nwdo).grid(row=16, column=6)

label = Label(root, text="             ").grid(row=4, column=8)

# label for June:-
lab = Label(root, text="June").grid(row=10, column=10, columnspan=7)

lb = Label(root, text="Mon").grid(row=11, column=10)
lb = Label(root, text="Tue").grid(row=11, column=11)
lb = Label(root, text="Wed").grid(row=11, column=12)
lb = Label(root, text="Thu").grid(row=11, column=13)
lb = Label(root, text="Fri").grid(row=11, column=14)
lb = Label(root, text="Sat").grid(row=11, column=15)
lb = Label(root, text="Sun").grid(row=11, column=16)

# Buttons for June:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=12, column=10)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=12, column=11)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=12, column=12)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=12, column=13)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=12, column=14)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=12, column=15)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=12, column=16)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=13, column=10)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=13, column=11)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=13, column=12)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=13, column=13)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=13, column=14)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=13, column=15)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=13, column=16)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=14, column=10)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=14, column=11)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=14, column=12)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=14, column=13)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=14, column=14)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=14, column=15)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=14, column=16)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=15, column=10)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=15, column=11)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=15, column=12)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=15, column=13)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=15, column=14)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=15, column=15)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=15, column=16)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=16, column=10)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=16, column=11)

label = Label(root, text="             ").grid(row=4, column=18)

# label for July:-
lab = Label(root, text="July").grid(row=10, column=20, columnspan=7)

lb = Label(root, text="Mon").grid(row=11, column=20)
lb = Label(root, text="Tue").grid(row=11, column=21)
lb = Label(root, text="Wed").grid(row=11, column=22)
lb = Label(root, text="Thu").grid(row=11, column=23)
lb = Label(root, text="Fri").grid(row=11, column=24)
lb = Label(root, text="Sat").grid(row=11, column=25)
lb = Label(root, text="Sun").grid(row=11, column=26)

# Buttons for July:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=12, column=22)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=12, column=23)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=12, column=24)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=12, column=25)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=12, column=26)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=13, column=20)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=13, column=21)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=13, column=22)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=13, column=23)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=13, column=24)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=13, column=25)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=13, column=26)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=14, column=20)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=14, column=21)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=14, column=22)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=14, column=23)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=14, column=24)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=14, column=25)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=14, column=26)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=15, column=20)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=15, column=21)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=15, column=22)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=15, column=23)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=15, column=24)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=15, column=25)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=15, column=26)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=16, column=20)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=16, column=21)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=16, column=22)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=16, column=23)

btn31 = Button(root, text="31", padx=12, pady=10, command=nwdo).grid(row=16, column=24)

label = Label(root, text="             ").grid(row=4, column=28)

# label for August:-
lab = Label(root, text="August").grid(row=10, column=30, columnspan=7)

lb = Label(root, text="Mon").grid(row=11, column=30)
lb = Label(root, text="Tue").grid(row=11, column=31)
lb = Label(root, text="Wed").grid(row=11, column=32)
lb = Label(root, text="Thu").grid(row=11, column=33)
lb = Label(root, text="Fri").grid(row=11, column=34)
lb = Label(root, text="Sat").grid(row=11, column=35)
lb = Label(root, text="Sun").grid(row=11, column=36)

# Buttons for August:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=12, column=35)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=12, column=36)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=13, column=30)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=13, column=31)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=13, column=32)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=13, column=33)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=13, column=34)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=13, column=35)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=13, column=36)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=14, column=30)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=14, column=31)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=14, column=32)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=14, column=33)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=14, column=34)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=14, column=35)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=14, column=36)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=15, column=30)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=15, column=31)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=15, column=32)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=15, column=33)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=15, column=34)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=15, column=35)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=15, column=36)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=16, column=30)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=16, column=31)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=16, column=32)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=16, column=33)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=16, column=34)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=16, column=35)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=16, column=36)

btn31 = Button(root, text="31", padx=12, pady=10, command=nwdo).grid(row=12, column=30)

# label for September:-
lab = Label(root, text="September").grid(row=20, column=0, columnspan=7)

lb = Label(root, text="Mon").grid(row=21, column=0)
lb = Label(root, text="Tue").grid(row=21, column=1)
lb = Label(root, text="Wed").grid(row=21, column=2)
lb = Label(root, text="Thu").grid(row=21, column=3)
lb = Label(root, text="Fri").grid(row=21, column=4)
lb = Label(root, text="Sat").grid(row=21, column=5)
lb = Label(root, text="Sun").grid(row=21, column=6)

# Buttons for september:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=22, column=1)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=22, column=2)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=22, column=3)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=22, column=4)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=22, column=5)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=22, column=6)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=23, column=0)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=23, column=1)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=23, column=2)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=23, column=3)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=23, column=4)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=23, column=5)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=23, column=6)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=24, column=0)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=24, column=1)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=24, column=2)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=24, column=3)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=24, column=4)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=24, column=5)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=24, column=6)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=25, column=0)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=25, column=1)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=25, column=2)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=25, column=3)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=25, column=4)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=25, column=5)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=25, column=6)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=26, column=0)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=26, column=1)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=26, column=2)

btn31 = Button(root, text="31", padx=12, pady=10, command=nwdo).grid(row=26, column=3)

label = Label(root, text="             ").grid(row=4, column=8)

# label for October:-
lab = Label(root, text="October").grid(row=20, column=10, columnspan=7)

lb = Label(root, text="Mon").grid(row=21, column=10)
lb = Label(root, text="Tue").grid(row=21, column=11)
lb = Label(root, text="Wed").grid(row=21, column=12)
lb = Label(root, text="Thu").grid(row=21, column=13)
lb = Label(root, text="Fri").grid(row=21, column=14)
lb = Label(root, text="Sat").grid(row=21, column=15)
lb = Label(root, text="Sun").grid(row=21, column=16)

# Buttons for October:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=22, column=13)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=22, column=14)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=22, column=15)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=22, column=16)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=23, column=10)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=23, column=11)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=23, column=12)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=23, column=13)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=23, column=14)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=23, column=15)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=23, column=16)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=24, column=10)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=24, column=11)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=24, column=12)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=24, column=13)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=24, column=14)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=24, column=15)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=24, column=16)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=25, column=10)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=25, column=11)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=25, column=12)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=25, column=13)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=25, column=14)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=25, column=15)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=25, column=16)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=26, column=10)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=26, column=11)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=26, column=12)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=26, column=13)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=26, column=14)

btn31 = Button(root, text="31", padx=12, pady=10, command=nwdo).grid(row=26, column=15)

label = Label(root, text="             ").grid(row=4, column=18)

# label for November:-
lab = Label(root, text="November").grid(row=20, column=20, columnspan=7)

lb = Label(root, text="Mon").grid(row=21, column=20)
lb = Label(root, text="Tue").grid(row=21, column=21)
lb = Label(root, text="Wed").grid(row=21, column=22)
lb = Label(root, text="Thu").grid(row=21, column=23)
lb = Label(root, text="Fri").grid(row=21, column=24)
lb = Label(root, text="Sat").grid(row=21, column=25)
lb = Label(root, text="Sun").grid(row=21, column=26)

# Buttons for November:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=22, column=26)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=23, column=20)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=23, column=21)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=23, column=22)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=23, column=23)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=23, column=24)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=23, column=25)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=23, column=26)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=24, column=20)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=24, column=21)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=24, column=22)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=24, column=23)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=24, column=24)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=24, column=25)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=24, column=26)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=25, column=20)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=25, column=21)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=25, column=22)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=25, column=23)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=25, column=24)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=25, column=25)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=25, column=26)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=26, column=20)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=26, column=21)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=26, column=22)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=26, column=23)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=26, column=24)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=26, column=25)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=26, column=26)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=22, column=20)

label = Label(root, text="             ").grid(row=4, column=28)

# label for December:-
lab = Label(root, text="December").grid(row=20, column=30, columnspan=7)

lb = Label(root, text="Mon").grid(row=21, column=30)
lb = Label(root, text="Tue").grid(row=21, column=31)
lb = Label(root, text="Wed").grid(row=21, column=32)
lb = Label(root, text="Thu").grid(row=21, column=33)
lb = Label(root, text="Fri").grid(row=21, column=34)
lb = Label(root, text="Sat").grid(row=21, column=35)
lb = Label(root, text="Sun").grid(row=21, column=36)

# Buttons for December:-
btn1 = Button(root, text="1", padx=15, pady=10, command=nwdo).grid(row=22, column=31)
btn2 = Button(root, text="2", padx=15, pady=10, command=nwdo).grid(row=22, column=32)
btn3 = Button(root, text="3", padx=15, pady=10, command=nwdo).grid(row=22, column=33)
btn4 = Button(root, text="4", padx=15, pady=10, command=nwdo).grid(row=22, column=34)
btn5 = Button(root, text="5", padx=15, pady=10, command=nwdo).grid(row=22, column=35)

btn6 = Button(root, text="6", padx=15, pady=10, command=nwdo).grid(row=22, column=36)
btn7 = Button(root, text="7", padx=15, pady=10, command=nwdo).grid(row=23, column=30)
btn8 = Button(root, text="8", padx=15, pady=10, command=nwdo).grid(row=23, column=31)
btn9 = Button(root, text="9", padx=15, pady=10, command=nwdo).grid(row=23, column=32)
btn10 = Button(root, text="10", padx=12, pady=10, command=nwdo).grid(row=23, column=33)
btn11 = Button(root, text="11", padx=12, pady=10, command=nwdo).grid(row=23, column=34)
btn12 = Button(root, text="12", padx=12, pady=10, command=nwdo).grid(row=23, column=35)

btn13 = Button(root, text="13", padx=12, pady=10, command=nwdo).grid(row=23, column=36)
btn14 = Button(root, text="14", padx=12, pady=10, command=nwdo).grid(row=24, column=30)
btn15 = Button(root, text="15", padx=12, pady=10, command=nwdo).grid(row=24, column=31)
btn16 = Button(root, text="16", padx=12, pady=10, command=nwdo).grid(row=24, column=32)
btn17 = Button(root, text="17", padx=12, pady=10, command=nwdo).grid(row=24, column=33)
btn18 = Button(root, text="18", padx=12, pady=10, command=nwdo).grid(row=24, column=34)
btn19 = Button(root, text="19", padx=12, pady=10, command=nwdo).grid(row=24, column=35)

btn20 = Button(root, text="20", padx=12, pady=10, command=nwdo).grid(row=24, column=36)
btn21 = Button(root, text="21", padx=12, pady=10, command=nwdo).grid(row=25, column=30)
btn22 = Button(root, text="22", padx=12, pady=10, command=nwdo).grid(row=25, column=31)
btn23 = Button(root, text="23", padx=12, pady=10, command=nwdo).grid(row=25, column=32)
btn24 = Button(root, text="24", padx=12, pady=10, command=nwdo).grid(row=25, column=33)
btn25 = Button(root, text="25", padx=12, pady=10, command=nwdo).grid(row=25, column=34)
btn26 = Button(root, text="26", padx=12, pady=10, command=nwdo).grid(row=25, column=35)

btn27 = Button(root, text="27", padx=12, pady=10, command=nwdo).grid(row=25, column=36)
btn28 = Button(root, text="28", padx=12, pady=10, command=nwdo).grid(row=26, column=30)
btn29 = Button(root, text="29", padx=12, pady=10, command=nwdo).grid(row=26, column=31)
btn30 = Button(root, text="30", padx=12, pady=10, command=nwdo).grid(row=26, column=32)

btn31 = Button(root, text="31", padx=12, pady=10, command=nwdo).grid(row=26, column=33)

root.mainloop()
