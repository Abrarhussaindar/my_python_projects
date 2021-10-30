from tkinter import * 
import tkinter.messagebox
import tkinter
root = Tk()
root.geometry("700x700")

#b1 = Button(root, text = "click here! ", bd = "10", command = root.destroy)
#b2 = Button(root, text = "click now ", bd = "10", command = root.image_names)


#can = Canvas(root, bg = "black", height = 800, width = 1600)
#Canvas = Canvas(root, height = 600, width = 400, bg = "black")

task1 = Checkbutton(root, text = input("enter your ist task "), onvalue = 1, offvalue = 0, height = 5, width = 20)
task2 = Checkbutton(root, text = input("enter your 2nd task "), onvalue = 1, offvalue = 0, height = 5, width = 20)
task3 = Checkbutton(root, text = input("enter your 3rd task "), onvalue = 1, offvalue = 0, height = 5, width = 20)
task4 = Checkbutton(root, text = input("enter your 4th task "), onvalue = 1, offvalue = 0, height = 5, width = 20)
task5 = Checkbutton(root, text = input("enter your 5th task "), onvalue = 1, offvalue = 0, height = 5, width = 20)
task6 = Checkbutton(root, text = input("enter your 6th task "), onvalue = 1, offvalue = 0, height = 5, width = 20)
task7 = Checkbutton(root, text = input("enter your 7th task "), onvalue = 1, offvalue = 0, height = 5, width = 20)
task8 = Checkbutton(root, text = input("enter your 8th task "), onvalue = 1, offvalue = 0, height = 5, width = 20)
task9 = Checkbutton(root, text = input("enter your 9th task "), onvalue = 1, offvalue = 0, height = 5, width = 20)
taskX = Checkbutton(root, text = input("enter your Xth task "), onvalue = 1, offvalue = 0, height = 5, width = 20)



task1.pack(side = "top")
task2.pack(side = "top")
task3.pack(side = "top")
task4.pack(side = "bottom")
task5.pack(side = "bottom")
task6.pack(side = "bottom")
task7.pack(side = "left")
task8.pack(side = "left")
task9.pack(side = "left")
taskX.pack(side = "left")


#b1.pack(side = "top")
#b2.pack(side = "left")

#can.pack()

root.mainloop()
