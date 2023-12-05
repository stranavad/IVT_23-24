import turtle
import random
import math
pen = turtle.Turtle() # hlavní pero na kreslení
pen.screen.colormode(255) # umožnění práce s RGB barvami
pen.penup() # pero je na začátku zdvižené
turtle.tracer(False)  # nebude viditelná animace, rovnou se vše vykreslí

pen.screen.bgcolor("blue") # barva pozadí - můžete přenastavit
                            # názvy všech barev najdete na: https://trinket.io/docs/colors


# zde definujte funkce

def draw_rectangle(a: int, b: int, color: str, x: int, y: int):
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()

    pen.forward(a)
    pen.left(90)
    pen.forward(b)
    pen.left(90)
    pen.forward(a)
    pen.left(90)
    pen.forward(90)
    pen.left(90)
    pen.end_fill()

def draw_snowflake(x,y, size):
    pen.goto(x,y)
    pen.pendown()
    pen.color("light sky blue")
    for i in range(8):
        pen.forward(size)
        pen.backward(size/3)
        pen.left(45)
        pen.forward(size/3)
        pen.backward(size/3)
        pen.right(90)
        pen.forward(size/3)
        pen.backward(size/3)
        pen.left(45)
        pen.backward(2*size/3)
        pen.right(45)
    pen.penup()

if __name__ == '__main__':
    for i in range(200):
        x = random.randint(math.floor(-1 * turtle.window_width() / 2), math.floor(turtle.window_width() / 2))
        y = random.randint(math.floor(-1 * turtle.window_height() / 2), math.floor(turtle.window_height() / 2))
        # zde pak hlavní tělo programu
        draw_snowflake(x + 10, y - 10, random.randint(3, 20))


    # Face
    draw_rectangle(91, 120, "moccasin", -45, 0)

    # ocicka
    draw_rectangle(10, 10, "green", -20, 75)
    draw_rectangle(10, 10, "green", 10, 75)

    # pusinka
    draw_rectangle(31, 10, "red", -15, 40)



    # klobouk overlays
    draw_rectangle(95, 124, "white", -47, 118)

    # klobouk
    draw_rectangle(91, 120, "red", -45, 120)

    # Kriz v klobouku
    # Horizontalni
    draw_rectangle(30, 7, "white", -15, 180)

    # Vertikalni
    draw_rectangle(7, 45, "white", -3, 155)

    # body
    draw_rectangle(121, -240, "white", -60, 0)
    draw_rectangle(91, -160, "red", -45, 0)

    # Kriz na hrudi
    # Horizontalni
    draw_rectangle(30, 7, "white", -15, -60)

    # Vertikalni
    draw_rectangle(7, 45, "white", -3, -85)

    # Right hand
    draw_rectangle(121, -25, "white", 60, 0)
    draw_rectangle(25, -25, "moccasin", 181, 0)

    # Stick
    draw_rectangle(7, -240, "brown", 195, 10)

    pen.goto(218, 25)
    pen.width(5)
    pen.pendown()
    pen.color("yellow")
    # pen.left(90)
    for i in range(1, 9):
        pen.forward(i * 5)
        pen.left(90)

    pen.penup()
    # pen.color("gold")

    # Left hand
    draw_rectangle(25, -121, "white", -85, 0)
    draw_rectangle(25, -25, "moccasin", -85, -121)


    turtle.done()  # aby se hned neukončilo okno s obrázkem