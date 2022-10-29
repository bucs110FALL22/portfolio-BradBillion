import turtle
import random

turt = turtle.Turtle()
window = turtle.Screen()
cloudNum = 10


def drawCloud(coord, bumps=3):
    turt.down()
    cloudP = 6
    cloudL = random.randrange(8, 11)
    magicNumber = 67
    turt.begin_fill()
    turt.fd(cloudL * 10)
    for n in range(bumps):
        for i in range(cloudP):
            angle = 200 / (n + 1)
            turt.lt(angle / cloudP)
            turt.fd(cloudL - (2 * n))
        turt.rt(magicNumber)
    turt.goto(coord)
    turt.end_fill()
    turt.seth(0)


def changePos():
    turt.up()
    screen = window.screensize()
    newX = random.randrange(-1 * screen[0], screen[0])
    newY = random.randrange(-1 * screen[1], screen[1])
    turt.goto(newX / 2, newY / 2)
    coord = (newX / 2, newY / 2)
    return coord


def main():
    window.bgcolor("lightblue")
    turt.shape("turtle")
    turt.color("white", "white")
    turt.speed(0)
    for i in range(cloudNum):
        drawCloud(changePos(), random.randrange(3, 7))
    turt.up()
    turt.goto(0, -400)


main()
window.exitonclick()
