import pygame
import os

class Settings():
    def __init__(self):
        self.W = 800
        self.H = 447
        self.win = pygame.display.set_mode((self.W, self.H))

        self.bg = pygame.image.load(os.path.join('images', 'backGround.png')).convert()
        self.bg = pygame.transform.scale(self.bg, (1214, 444))
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        self.gameActive = True

    # for variables that will change throughout the game
    def initDynamicSettings(self):
        self.pause = 0
        self.speed = 30
        self.score = 0

    # for variables that I want to set at different times than the variables in intiDynamicSettings
    def initOtherSettings(self):
        self.fallSpeed = 0

    # I think this is the waiting period between when the runner hits an object and the endscreen
    def addPause(self):
        self.pause += 1

    def getSpeed(self):
        return self.speed

    def setFallSpeed(self, num):
        self.fallSpeed = num

    def setPause(self, num):
        self.pause = num

    def increaseSpeed(self):
        self.speed += 1

    # updates rolling screen so it goes back every update (gives impression of movement)
    def rollingScreen(self):
        self.bgX -= 1.4
        self.bgX2 -= 1.4
        if (self.bgX < self.bg.get_width() * -1):
            self.bgX = self.bg.get_width()
        if (self.bgX2 < self.bg.get_width() * -1):
            self.bgX2 = self.bg.get_width()

    def getSpeed(self):
        return self.speed
        
