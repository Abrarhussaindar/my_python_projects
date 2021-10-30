from  tkinter import *
root = Tk()

root.title("Calculator")

e = Entry(root, width = 73, borderwidth = 15)
e.grid(row = 0, column = 0, columnspan = 30, ipady = 30)

#defing the process
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

#def button_dot():
 #   second_number = float(e.get())
  #  e.delete(0, END)


    if math == "add":
        e.insert(0, f_num + int(second_number))
    if math == "subtract":
        e.insert(0, f_num - int(second_number))
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
    if math == "divide":
        e.insert(0, f_num / int(second_number))
    if math == "sqr":
        e.insert(0, f_num**2)
    if math == "sqrt":
        e.insert(0, f_num**(1/2.0))
    if math == "percentage":
        e.insert(0, f_num % int(second_number))
    #if math == "dot":
    #    e.insert(0, f_num . second_number)
   



def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)

def button_sqr():
    first_number = e.get()
    global f_num
    global math
    math = "sqr"
    f_num = int(first_number)
    e.delete(0, END)

def button_sqrt():
    first_number = e.get()
    global f_num
    global math
    math = "sqrt"
    f_num = int(first_number)
    e.delete(0, END)

def button_percentage():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    e.delete(0, END)

#def button_dot():
 #   first_number = e.get()
  #  global f_num
   # global math
    #math = "dot"
    #f_num = float(first_number)
    #e.delete(0, END)

#making buttons
button_1 = Button(root, text = "1", padx = 50, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 50, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 50, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 50, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 50, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 50, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 50, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 50, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 50, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 50, pady = 20, command = lambda: button_click(0))



button_equal = Button(root, text = "=", padx = 50, pady = 20, command = button_equal)
button_clear = Button(root, text = "C", padx = 48, pady = 20, command = button_clear)


button_add = Button(root, text = "+", padx = 49, pady = 20, command = button_add)
button_subtract = Button(root, text = "-", padx = 50, pady = 20, command = button_subtract)
button_multiply = Button(root, text = "*", padx = 50, pady = 20, command = button_multiply)
button_divide = Button(root, text = "/", padx = 50, pady = 20, command = button_divide)
button_percentage = Button(root, text = "%", padx = 47, pady = 20, command = button_percentage)
button_sqr = Button(root, text = "sqr", padx = 45, pady = 20, command = button_sqr)
button_sqrt = Button(root, text = "sqrt", padx = 43, pady = 20, command = button_sqrt)

button_quit = Button(root, text = "Exit", padx = 44, pady = 20, command=root.quit)
#button_dot = Button(root, text = ".", padx = 52, pady = 20, command=button_dot)


#displaying buttons
button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)

button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)

button_0.grid(row = 5, column = 0)

button_equal.grid(row = 5, column = 1)


button_add.grid(row = 5, column = 4)
button_subtract.grid(row = 4, column = 4)
button_multiply.grid(row = 3, column = 4)
button_divide.grid(row = 2, column = 4)
button_sqr.grid(row = 1, column = 1)
button_sqrt.grid(row = 1, column = 2)
button_clear.grid(row = 1, column = 4)
button_percentage.grid(row = 1, column = 0)

#button_dot.grid(row = 5, column = 2)
button_quit.grid(row = 5, column = 2)

root.mainloop()