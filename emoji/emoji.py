from dot_location import dot_locations
import turtle

eyes_locations = [
    [45, 120],
    [-45, 120]
]
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Smiley")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.speed(200)
my_turtle.shape("circle")

def draw_circle(radius, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def move_turtle(x, y):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()

draw_circle(100, "black", "yellow")

for location in eyes_locations:
    move_turtle(location[0], location[1])
    draw_circle(10,  "black", "black")

for location in dot_locations:
    move_turtle(location[0], location[1])
    draw_circle(2, "black", "black")

my_turtle.hideturtle()
turtle.done()