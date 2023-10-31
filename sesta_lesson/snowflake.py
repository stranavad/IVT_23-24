import turtle
from random import randint

SIZE = 75
SMALL = 140
LARGE = 40

def run():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    t.color("#b0e0e6")
    t.width(3)
    t.hideturtle()

    for i in range(15):
        t.forward(SIZE)
        t.left(LARGE)
        t.forward(SIZE)
        t.left(SMALL)
        t.forward(SIZE)
        t.left(LARGE)
        t.forward(SIZE)
        t.left(SMALL)
        t.left(24)

    turtle.done()


if __name__ == '__main__':
    run()
