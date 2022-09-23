import turtle  #1. import modules
import random
import time
import pygame
import math

#Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor('lightblue')

turtA = turtle.Turtle()  # 3.  Create two turtles
turtB = turtle.Turtle()
turtC = turtle.Turtle()
turtA.color('red')
turtB.color('blue')
turtC.color('black')
turtA.shape('turtle')
turtB.shape('turtle')
turtC.shape('turtle')

turtA.up()  # 4. Pick up the pen so we don’t get lines
turtB.up()
turtC.up()
turtA.goto(-100, 20)
turtB.goto(-100, -20)
turtC.goto(-80, 40)
turtC.down()
turtC.goto(-80, -40)
turtC.up()
turtC.goto(80, 40)
turtC.down()
turtC.goto(80, -40)
turtC.up()
turtC.goto(100, 0)
turtC.left(180)
## 5. Your PART A code goes here
print("")
race1 = True
race2 = False
print("Starting Race 1")
turtA.down()
turtB.down()
for i in range(4):
    if i == 3:
        print("Go!")
    else:
        print(3 - i)
        time.sleep(1)
turtA.forward(random.randrange(1, 201))
turtB.forward(random.randrange(1, 201))
time.sleep(1)
if turtA.xcor() > turtB.xcor():
    print("Red wins!")
elif turtB.xcor() > turtA.xcor():
    print("Blue Wins!")
elif turtB.xcor() == turtA.xcor():
    print("It's a Tie!")
time.sleep(3)
turtA.clear()
turtB.clear()
turtA.up()
turtB.up()
turtA.left(180)
turtB.left(180)
turtA.goto(-100, 20)
turtB.goto(-100, -20)
turtA.left(180)
turtB.left(180)
race1 = False
race2 = True
print("Moving on the Race 2")
turtA.down()
turtB.down()
for i in range(4):
    if i == 3:
        print("Go!")
    else:
        print(3 - i)
        time.sleep(1)
while race2 == True:
    turtA.forward(random.randrange(1, 10))
    time.sleep(0.075)
    if turtA.xcor() >= 90 or turtB.xcor() >= 90:
        race2 = False
        break
    turtB.forward(random.randrange(1, 10))
    time.sleep(0.2)
    if turtA.xcor() >= 90 or turtB.xcor() >= 90:
        race2 = False
        break
    turtB.forward(random.randrange(1, 10))
    time.sleep(0.075)
    if turtA.xcor() >= 90 or turtB.xcor() >= 90:
        race2 = False
        break
    turtA.forward(random.randrange(1, 10))
    time.sleep(0.2)
    if turtA.xcor() >= 90 or turtB.xcor() >= 90:
        race2 = False
        break
if turtA.xcor() > turtB.xcor():
    print("Red wins!")
elif turtB.xcor() > turtA.xcor():
    print("Blue Wins!")
elif turtB.xcor() == turtA.xcor():
    print("It's a Tie!")
time.sleep(1)
print("That concludes our Races!")
time.sleep(3)
turtA.clear()
turtB.clear()
turtA.up()
turtB.up()
turtA.left(180)
turtB.left(180)
turtA.goto(-100, 20)
turtB.goto(-100, -20)
turtA.left(180)
turtB.left(180)

print("Click to Continue to Part B")
window.exitonclick()

# PART B - complete part B here
pygame.init()
pyWindow = pygame.display.set_mode()

numSides = [3, 4, 6, 9, 360]
sideLength = 100
offset = 100

for n in numSides:
    pyWindow.fill("black")
    coords = [
        0,
    ] * n

    for i in range(n):

        theta = (2 * math.pi * (i)) / n
        x = sideLength * math.cos(theta) + offset
        y = sideLength * math.sin(theta) + offset
        coords[i] = (x, y)
    pygame.draw.polygon(pyWindow, "red", coords)
    pygame.display.flip()
    pygame.time.wait(2000)
