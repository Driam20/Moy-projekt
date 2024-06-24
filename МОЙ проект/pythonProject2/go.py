import turtle

def move(a):
    turtle.forward(a)
    turtle.left(90)

def drawSquareColor(a,color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        move(a)
    turtle.end_fill()

turtle.speed(1)

drawSquareColor(60, "red")
turtle.goto(150,150)
drawSquareColor(100, "blue")
