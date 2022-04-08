import time
import turtle
from turtle import Turtle
from random import randint

#Window Setup
window = turtle.Screen()
window.title("TURTLE RACE")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-200,200)
turtle.write("TURTLE RACE",font=("Arial", 30, "bold"))
turtle.penup()

#Finish Line
stamp_size = 20
square_size = 15
finish_line = 200
turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150 - (i*square_size*2)))
    turtle.stamp()
    
for j in range(10):
    turtle.setpos(finish_line+square_size, ((150-square_size)-(j*square_size*2)))
    turtle.stamp()
turtle.hideturtle()

#Turtle 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("cyan")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()

#Turtle 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("yellow")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

#Turtle 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("orange")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

#Turtle 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("red")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()

#Turtle 5
turtle5 = Turtle()
turtle5.speed(0)
turtle5.color("white")
turtle5.shape("turtle")
turtle5.penup()
turtle5.goto(-250, -100)
turtle5.pendown()

time.sleep(1)

# Moving the turtles
for x in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))
    turtle5.forward(randint(1,5))

#Finding the winner
if turtle1.xcor()>turtle2.xcor() and turtle1.xcor()>turtle3.xcor() and turtle1.xcor()>turtle4.xcor() and turtle1.xcor()>turtle5.xcor() :
    print("Blue turtle wins!")
    for x in range(72):
        turtle1.right(5)
elif turtle2.xcor()>turtle1.xcor() and turtle2.xcor()>turtle3.xcor() and turtle2.xcor()>turtle4.xcor() and turtle2.xcor()>turtle5.xcor() :
    print("Yellow turtle wins!")
    for x in range(72):
        turtle2.right(5)
elif turtle3.xcor()>turtle2.xcor() and turtle3.xcor()>turtle1.xcor() and turtle3.xcor()>turtle4.xcor() and turtle3.xcor()>turtle5.xcor() :
    print("Orange turtle wins!")
    for x in range(72):
        turtle3.right(5)
elif turtle4.xcor()>turtle2.xcor() and turtle4.xcor()>turtle3.xcor() and turtle4.xcor()>turtle1.xcor() and turtle4.xcor()>turtle5.xcor() :
    print("Red turtle wins!")
    for x in range(72):
        turtle4.right(5)
else:
    print("White turtle wins!")
    for x in range(72):
        turtle5.right(5)

turtle.exitonclick()