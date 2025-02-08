from turtle import * 

v = 100

kaplumbaga = Turtle()
kaplumbaga.color("blue")
kaplumbaga.width(5)
kaplumbaga.shape("circle")
kaplumbaga.pendown()
kaplumbaga.speed(v)

def draw(x,y):
    kaplumbaga.goto(x,y)

def move(x,y):
    kaplumbaga.penup()
    kaplumbaga.goto(x,y)
    kaplumbaga.pendown()

def setRed():
    kaplumbaga.color("red")

def setGreen():
    kaplumbaga.color("green")

def startFill():
    kaplumbaga.begin_fill()

def endFill():
    kaplumbaga.end_fill()
    
kaplumbaga.ondrag(draw)
screen = kaplumbaga.getscreen()
screen.onscreenclick(move)
screen.onkey(setRed, "r")
screen.onkey(setGreen,"g")
screen.onkey(startFill,"f")
screen.onkey(endFill,"e")
screen.listen()
