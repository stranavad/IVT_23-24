import turtle

SQUARE_SIZE = 100

def run():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.width(2)
    t.hideturtle()

    for i in range(4):
        t.forward(SQUARE_SIZE)
        t.left(90)

    turtle.done()


if __name__ == '__main__':
    run()
