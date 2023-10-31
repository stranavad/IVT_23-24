import turtle

SHAPE_SIZE = 100

def run():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.width(2)
    t.hideturtle()
    t.penup()
    t.backward(600)
    t.penup()

    shapes = [3, 4, 5, 6, 7]

    for shape in shapes:
        t.pendown()
        for i in range(shape):
            t.forward(SHAPE_SIZE)
            t.left(360 / shape)

        t.penup()
        t.forward(3 * SHAPE_SIZE)

    turtle.done()


if __name__ == '__main__':
    run()
