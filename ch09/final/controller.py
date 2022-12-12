from textDraw import drawText
import random
import html


class Controller():

    def __init__(self, pygame, proxy, colors, font, screen, screenSize):
        self.pygame = pygame
        self.proxy = proxy
        self.colors = colors
        self.bkg = self.colors[0]
        self.font = font
        self.screen = screen
        self.SS = screenSize
        self.currentFact = ""
        self.emojis = ""
        self.eventLoop()

    def eventLoop(self):
        pygame = self.pygame
        running = True
        timeSinceFact = 0  #amount of updates since the last fact was given
        #Putting Click for a New Fact on a surface
        txt_surf = pygame.Surface((self.SS[0], self.SS[1]), pygame.SRCALPHA)
        clear = pygame.Color(255, 255, 255, 0)
        txt_surf.fill(clear)
        text = self.font.render("~ Click for a New Fact ~", False,
                                pygame.Color(255, 255, 255, 50))
        textRect = text.get_rect(center=(self.SS[0] * 0.5, self.SS[1] * 0.8))
        txt_surf.blit(text, textRect)

        # font for emojis...
        # ended up not working bc pygame doesnt support rendering emojis
        emjFont = pygame.font.SysFont('segoeuiemoji', int(self.SS[0] * 0.05))

        def newFact():  #fetches a new fact from the random fact API
            self.screen.fill("black")
            text = self.font.render("loading...", False, "white")
            textRect = text.get_rect(center=(self.SS[0] * 0.5,
                                             self.SS[1] * 0.5))
            self.screen.blit(text, textRect)
            pygame.display.update()
            self.currentFact = self.proxy.newFact()
            self.bkg = self.colors[random.randrange(0, len(self.colors))]
            print(" ")
            print("~~ NEW FACT ~~")
            print(self.currentFact)
            findEmojis()

        def findEmojis():  #finds relevant emojis using the words from the fact
            listOfWords = self.currentFact.split()
            emojiList = []
            self.emojis = ""
            for word in listOfWords:
                emoji = self.proxy.getEmoji(word)
                if emoji != None:
                    un = str(emoji['htmlCode'])  # isolates emoji html code
                    emj = html.unescape(un[2:(len(un) - 2)])
                    #html unescape turns the code into the respective character
                    emojiList.append(emj)
                    self.emojis += emj
            print("Emojis:", emojiList)

        def updateScreen(
        ):  # reblits everything to the screen, called every frame
            pygame = self.pygame
            self.screen.fill(self.bkg)
            textRect = pygame.Rect(self.SS[0] * 0.1, self.SS[1] * 0.1,
                                   self.SS[0] * 0.8, self.SS[1] * 0.5)
            #draw text function makes sure the text doesnt spill over sides.
            drawText(self.screen, f"{self.currentFact}", "white", textRect,
                     self.font)
            text = emjFont.render(f"{self.emojis}", False, "white")
            textRect = text.get_rect(center=(self.SS[0] * 0.5,
                                             self.SS[1] * 0.7))
            self.screen.blit(text, textRect)

            #Using the time to make the text oscillate between transparent and opaque
            if timeSinceFact >= 200:
                alphaValue = abs((pygame.time.get_ticks() % 1000) - 500) / 500
                txt_surf.set_alpha(255 * alphaValue)
            else:
                txt_surf.set_alpha(0)
            self.screen.blit(txt_surf, (0, 0))

            pygame.display.update()

        newFact()  #calls new fact right before loop starts

        while running:
            updateScreen()
            timeSinceFact += 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    newFact()
                    timeSinceFact = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                        break
                    if event.key == pygame.K_RETURN:
                        newFact()
