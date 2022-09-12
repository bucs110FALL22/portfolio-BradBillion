import turtle

myTurtle = turtle.Turtle()
window = turtle.Screen()

myTurtle.shape("turtle")
myTurtle.color("blue")

myTurtle.color(input("Choose a color for the turtle: "))
numSides = int(input("Input the number of sides: "))
sideLength = float(input("Input the length of each side: "))

for i in range(numSides):
  myTurtle.forward(sideLength)
  myTurtle.left(360/numSides)
#} end of block

#turtle goes to the center of the shape
myTurtle.up()
myTurtle.forward(sideLength/2)
myTurtle.left(90)
myTurtle.forward((numSides/4)*(sideLength/2))

window.exitonclick()