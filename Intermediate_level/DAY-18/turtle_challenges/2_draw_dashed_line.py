from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("coral")

screen = Screen()

for _ in range(30):
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()
    tim.forward(10)

screen.exitonclick()