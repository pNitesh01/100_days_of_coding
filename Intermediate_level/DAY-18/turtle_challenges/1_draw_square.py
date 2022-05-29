from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("coral")

screen = Screen()

for _ in range(4):
    tim.forward(100)
    tim.left(90)

screen.exitonclick()