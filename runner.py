import pygame
import os


class Runner(object):
    run = [pygame.image.load(os.path.join('images/running', "Run__00" + str(x) + '.png')) for x in range(1, 7)]
    jump = [pygame.image.load(os.path.join('images/jumping', "Jump__00"+ str(x)  + '.png')) for x in range(0, 7)]
    slide = [pygame.image.load(os.path.join('images', 'sl5.png'))]
    fall = pygame.image.load(os.path.join('images', '0.png'))
    jumpList = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2,
                -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4,
                -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 1
        self.slideUp = False
        self.falling = False

    # for restarting the player
    def centerRunner(self):
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 1
        self.slideUp = False
        self.falling = False
        self.y = 300

    # updates runners position/image
    def draw(self, win):
        if self.falling:
            win.blit(self.fall, (self.x, self.y + 30))
        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount // 22], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 132:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 4, self.y, self.width-24, self.height - 10)
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount > 90 and self.slideCount < 110:
                self.y -= 1
            elif self.slideCount == 80:
                self.sliding = False
                self.slideUp = True
            elif self.slideCount > 20 and self.slideCount < 80:
                self.hitbox = (self.x , self.y + 3, self.width - 8, self.height - 35)

            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 1
                self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)
            win.blit(self.slide[0], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 1
            win.blit(self.run[self.runCount // 16], (self.x, self.y))
            self.runCount += 1
            self.hitbox = (self.x + 10, self.y, self.width -15, self.height - 13)
            
            
