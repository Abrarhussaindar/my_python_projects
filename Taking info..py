class trying(object):
    def __init__(self, name, age, roll_number, section, branch):
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.section = section
        self.branch = branch

    def speaking(self):
        print("\n" + "\n" +  "Hay! its me " +  self.name + "." + "\n" + "I'm " + self.age + " years old" + "." + "\n" + "My Roll number is: " + self.roll_number + "." + "\n" + 
            "I'm in Section: " + self.section + " " + "in Branch " + self.branch + "\n" + "\n")
 
for i in range(0, 10):
    object1 = trying(input("Enter your name: "), str(input("Enter your age: ")), str(input("Enter your roll number: ")), str(input("IN which section your: ")), str(input("In which branch your are: ")))
    object1.speaking()