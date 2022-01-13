import turtle 
import time
import random

screen = turtle.Screen()
screen.setup(1200, 700)
screen.bgcolor('black')
screen.title('Estrellas')

delay = 0.1
distance = 10
starSize = 6

star = []
lastStar = []

#-----------------------------

def newStar():

    if len(star) > 0:
        star.clear()

    x = random.randint(-500, 500)
    y = random.randint(-200, 200)

 
    point1 = [x,y]
    print("point1{}".format(point1))
    star.append(point1)
    

    for i in range (0, starSize):
        
        if i == (starSize - 1):
            point2 = [x, y + (i + distance * i)]
            star.append(point2)
            point5 = [x - (i + distance * i), y]
            star.append(point5)
            point3 = [x, y - (i + distance * i)]
            star.append(point3)
            point8 = [x + (i + distance * i), y]
            star.append(point8)
        else:
            point2 = [x, y + (i + distance * i)]
            star.append(point2)
            point5 = [x - (i + distance * i), y]
            star.append(point5)
            point3 = [x, y - (i + distance * i)]
            star.append(point3)
            point8 = [x + (i + distance * i), y]
            star.append(point8)
            point4 = [x - (i + distance * i), y + (i + distance * i)]
            star.append(point4)
            point6 = [x - (i + (distance * i)), y - (i + distance * i)]
            star.append(point6)
            point9 = [x + (i + distance * i), y - (i + distance * i)]
            star.append(point9)  
            point7 = [x + (i + distance * i), y + (i + distance * i)]
            star.append(point7)

    paintStar()
    time.sleep(delay)
    clearStar()


def newPoint(x, y):

    point = turtle.Turtle()
    point.hideturtle()
    point.shape('circle')
    point.color(newColor())
    point.shapesize(0.3)
    point.speed(60)
    point.penup()
    point.goto(x, y)
    lastStar.append(point)
    point.showturtle()

def newColor():
    c = random.randint(0, 5)
    color = 'white'
    if c == 0:
        color = '#991F60'
    elif c == 1:
        color = '#CC669C'
    elif c == 2:
        color = '#C22779'
    elif c == 3:
        color = '#E695C0'
    elif  c == 4:
        color = '#851B53'
    
    return color

def paintStar():
    for i in star:
        x = (i[0])
        y = (i[1])
        newPoint(x, y)

def clearStar():

    for i in lastStar:
        i.hideturtle()

    if len(lastStar) > 0:
        lastStar.clear()
       
 

while True: 
    newStar()
    time.sleep(delay)
    
