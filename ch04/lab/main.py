import pygame
import math
import random

pygame.init
window = pygame.display.set_mode()
window.fill("black")
screenSize = pygame.display.get_window_size()
x = screenSize[0]
y = screenSize[1]
if x > y:
    r = y / 2
elif y > x:
    r = x / 2
else:
    r = x / 2
players = ["red", "blue"]
redScore = 0
blueScore = 0
screenRect = pygame.Rect(0, 0, x, y)

#Part C
playerChoice = ""
leftRect = pygame.Rect(0, 0, x / 2, y)
rightRect = pygame.Rect(x / 2, 0, x / 2, y)
redBtn = pygame.draw.rect(window, "red", leftRect)
blueBtn = pygame.draw.rect(window, "blue", rightRect)
pygame.display.flip()
print("Who do you think will win?")
print("Red or Blue?")
awaitingGuess = True
while awaitingGuess == True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < x / 2:
                playerChoice = "red"
                awaitingGuess = False
                # pygame.draw.rect(window, "white", leftRect)
                # pygame.display.flip()
                # pygame.time.wait(100)
                # pygame.draw.rect(window, "red", leftRect)
                # pygame.display.flip()
                # pygame.time.wait(200)
                # pygame.draw.rect(window, "red", screenRect)

            elif event.pos[0] > x / 2:
                playerChoice = "blue"
                awaitingGuess = False
                # pygame.draw.rect(window, "white", rightRect)
                # pygame.display.flip()
                # pygame.time.wait(100)
                # pygame.draw.rect(window, "blue", rightRect)
                # pygame.display.flip()
                # pygame.time.wait(200)
                # pygame.draw.rect(window, "blue", screenRect)
print("You chose", playerChoice)
pygame.display.flip()
pygame.time.wait(500)

#Part A
window.fill("black")
pygame.draw.circle(window, "white", (x / 2, y / 2), r)
pygame.display.flip()
print("Starting Simulation")
pygame.time.wait(1000)

#Part B
winner = ""
for n in range(10):
    print("Round", str(n + 1))
    for player in players:
        cor = (random.randrange(0, x), random.randrange(0, y))
        # print(player + ":", cor[0], cor[1])
        disCenter = math.sqrt((cor[0] - x / 2)**2 + (cor[1] - y / 2)**2)
        inCircle = disCenter <= r
        if inCircle:
            print(player, "Hit!")
            pygame.draw.circle(window, player, cor, 5)
            if player is players[0]:
                redScore += 1
            if player is players[1]:
                blueScore += 1
        else:
            print(player, "Miss!")
            pygame.draw.circle(window, "gray", cor, 3)
        pygame.display.flip()
        pygame.time.wait(1000)
    if n == 9:
        if redScore > blueScore:
            print(players[0], "has won!")
            winner = players[0]
        if blueScore > redScore:
            print(players[1], "has won!")
            winner = players[1]
        if redScore == blueScore:
            print("They tied!")
        pygame.time.wait(1000)
    pygame.time.wait(1000)

# Part C Again
if winner is playerChoice:
    print("You were Right!")
    print("You Win!")
else:
    print("You were wrong...")
    print("You lost.")
pygame.time.wait(4000)