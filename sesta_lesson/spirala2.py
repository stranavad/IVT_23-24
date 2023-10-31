import turtle
from random import randint

TURNS = 1500
BASE_SIZE = 1
SHAPE = 3

def run():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)

    t.color("blue")
    turtle.colormode(255)
    t.width(1)
    t.hideturtle()

    for turn in range(TURNS):
        t.forward(BASE_SIZE + turn * 1)
        t.left(360 / SHAPE - 1)
        t.color(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )

    turtle.done()


if __name__ == '__main__':
    run()
