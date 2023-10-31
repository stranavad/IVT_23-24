import turtle
from random import randint

SIZE = 50
SUB_SIZE = 25
ANGLE = 45

def run():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.color("#b0e0e6")
    t.width(3)
    t.hideturtle()


    for i in range(8):
        draw_flake(t)
        draw_flake(t)
        t.forward(SUB_SIZE)
        t.backward(SUB_SIZE + 2 * SIZE)

        t.left(45)


    turtle.done()


def draw_flake(t):
    t.forward(SIZE)
    t.right(ANGLE)
    t.forward(SUB_SIZE)
    t.backward(SUB_SIZE)
    t.left(2 * ANGLE)
    t.forward(SUB_SIZE)
    t.backward(SUB_SIZE)
    t.right(ANGLE)


if __name__ == '__main__':
    run()
