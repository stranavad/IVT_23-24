import turtle
from random import randint

TURNS = 750
TURN_SIZE = 1

def run():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)

    t.color("blue")
    turtle.colormode(255)
    t.width(2)
    t.hideturtle()

    for i in range(1, TURNS + 1):
        t.forward(i * TURN_SIZE)
        t.right(90)
        t.color(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )

    turtle.done()


if __name__ == '__main__':
    run()
