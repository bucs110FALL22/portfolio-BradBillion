import turtle
import random
import time

window = turtle.Screen()
window.setup(300, 300)
window.bgcolor('lightblue')
turt = turtle.Turtle()
turt.shape("turtle")

running = True
while running is True:
    print(turt.xcor(), turt.ycor())
    direction = random.randrange(1, 3)
    if direction == 1:
        print("Heads")
        turt.left(90)
    elif direction == 2:
        print("Tails")
        turt.left(-90)
    turt.forward(50)
    print(turt.xcor(), turt.ycor())
    if turt.xcor() >= 150 or turt.xcor() <= -150:
        print("Out of Bounds")
        running = False
    elif turt.ycor() >= 150 or turt.ycor() <= -150:
        print("Out of Bounds")
        running = False
    else:
        print("Safe")
    time.sleep(1)

window.exitonclick()
