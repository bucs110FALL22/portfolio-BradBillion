import turtle


def drawEqShape(t, n, s):
    for i in range(n):
        t.forward(s)
        t.left(360 / n)


turt = turtle.Turtle()
window = turtle.Screen()
turt.shape("turtle")
turt.color("green")
numSides = int(input("Number of Sides? "))
sideLength = int(input("Length of each Side? "))
drawEqShape(turt, numSides, sideLength)
window.exitonclick()
