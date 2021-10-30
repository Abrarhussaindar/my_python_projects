from tkinter import *
import tkinter
import sqlite3
import datetime

root = Tk()
root.title("To Do List")
root.geometry("450x600")
root.configure(background="#2196f3")

added_time = str(datetime.datetime.now())
print("time is: " + added_time)

# database


# function to del record.
def delete():
    conn = sqlite3.connect("task_list.db")
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    conn.commit()
    conn.close()


# # creates  a database or connect to one
conn = sqlite3.connect("task_list.db")

# # creates cursor
c = conn.cursor()


# #
# #
# # # creates a table
# c.execute("""CREATE TABLE addresses (
#         text_field text,
#         added text
#         )""")


def on_Submit():
    # creates  a database or connect to one
    conn = sqlite3.connect("task_list.db")

    # creates cursor
    c = conn.cursor()

    # inserts into cna
    c.execute("INSERT INTO addresses VALUES (:text_field, :added)",
              {

                  'text_field': task_ent.get(),
                  'added': added_time
              })

    # commit changes
    conn.commit()

    # closes the connection
    conn.close()

    task_ent.delete(0, END)






def resul():
    conn = sqlite3.connect("task_list.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    print_record = ""
    for record in records:
        print_record += str(record[2]) + ". " + str(record[0]) + "\n"

    result_label = Label(root, text=print_record, bg="green", fg="black", font=20)
    result_label.grid(row=8, column=0, columnspan=3)

    # commit changes
    conn.commit()

    # closes the connection
    conn.close()


task_label = Label(root, text="Enter Your Task", bg="#2196f3", font=20, fg="white")
task_label.grid(row=0, column=0, padx=3, stick=N + W)
task_ent = Entry(root, width=40, font=20, borderwidth=5)
task_ent.grid(row=1, column=0, ipady=10)

btn = Button(root, text="Submit", command=on_Submit, bg="cyan", font=20).grid(row=2, column=0, padx=3, columnspan=2,
                                                                              stick=N + W, pady=10)

delete_box_label = Label(root, text="Enter Id Number To Delete Task", bg="#2196f3", fg="white", font=20)
delete_box_label.grid(row=4, column=0, padx=3, stick=N + W)
delete_box = Entry(root, width=30)
delete_box.grid(row=5, column=0, ipady=8,stick=N + W, padx=3)

btn_del = Button(root, text="Delete Id", command=delete, bg="cyan", font=20)
btn_del.grid(row=6, column=0, padx=3, stick=N + W)

btn_res = Button(root, text="Show Tasks", command=resul, bg="cyan", font=20).grid(row=7, column=0, padx=3, columnspan=2,
                                                                                   stick=N + W, pady=10)

# commit changes
conn.commit()

# closes the connection
conn.close()

root.mainloop()
