import turtle

cir_locations = [
    [50, 0],
    [-50, 0],
    [0, 50],
    [0, -50],
    [50, 50],
    [-50, 50],
    [50, -50],
    [-50, -50],
    [20, -40],
    [-20, -40],
    [-20, 40],
    [20, 40],
    [40, -20],
    [40, 20],
    [-40, 20],
    [-40, -20],
]
circ_loc = [
    [0,-69]
]

cir_turtle = turtle.Turtle()

def circle():
    cir_turtle.speed(50)
    cir_turtle.circle(50)
    
circle()

def move_turtle(x, y):
    cir_turtle.up()
    cir_turtle.goto(x, y)
    cir_turtle.down()
    
for location in cir_locations:
    move_turtle(location[0], location[1])
    circle()

def cirle():
    cir_turtle.circle(119)

for location in circ_loc:
    move_turtle(location[0], location[1])
    cirle()

cir_turtle.hideturtle()
turtle.done()