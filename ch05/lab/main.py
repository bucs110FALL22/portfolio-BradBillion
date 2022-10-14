import pygame

pygame.init()

iterList = {}
coordPairs = []
scaleX = 0
scaleY = 0
largest = [0, 0]


def tnp1(num):
    count = 0
    done = False
    while done == False:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (3 * num) + 1
        count += 1
        if num == 1:
            done = True
            return count


uL = int(input("Provide upper limit: "))

display = pygame.display.set_mode()
display.fill("white")
screenSize = pygame.display.get_window_size()
scaleX = screenSize[0] / uL

for i in range(2, uL):
    iterList[i] = tnp1(i)
    if iterList[i] > largest[1]:
        largest[0] = i
        largest[1] = iterList[i]

print(iterList)
scaleY = screenSize[1] / largest[1]
tscale = screenSize[1] / 20
font1 = pygame.font.Font(None, int(tscale))

for k, v in iterList.items():
    x = scaleX * k
    y = screenSize[1] - (scaleY * v)
    coordPairs.append((x + (scaleX / 10), y + (scaleY / 3)))
    if k >= 3:
        pygame.draw.lines(display, "red", False, coordPairs, width=1)
    msg = "(" + str(k) + ", " + str(v) + ")"
    coord = font1.render(msg, False, "black")
    display.blit(coord, (x, y))
    pygame.display.flip()
    pygame.time.wait(200)

dispMsg = "Highest Count: " + str(largest[0]) + ", " + str(largest[1])
font2 = pygame.font.Font(None, int(2 * tscale))
msgObj = font2.render(dispMsg, True, "purple")
display.blit(msgObj, (0, 0))

pygame.display.flip()
pygame.time.wait(5000)
