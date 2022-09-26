from turtle import *

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(100)


def move_backwards():
    tim.backward(100)


def counter_clock():

    c_clockwise = tim.heading() + 10
    tim.setheading(c_clockwise)


def move_clockwise():

    clockwise = tim.heading() - 10
    tim.setheading(clockwise)


def screen_clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=screen_clear)
screen.exitonclick()
