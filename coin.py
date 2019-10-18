import pygame
from pygame.sprite import Sprite

class Coin(Sprite):
    img = pygame.image.load('images/coin.png')

    def __init__(self, x, y, width, height):
        super(Coin, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.score = 0

    # checks to see if runner hits coins
    def collide(self, rect):
        if(rect[0] >= self.x and rect[0] + rect[2] <= self.x + self.width) or (rect[0] + 45 <= self.x and rect[0] + rect[2] >= self.x):
            if(rect[1] + 15 >= self.y and rect[3] <= self.height):
                return True
        return False

    # checks to see if coin is out of frame
    def update(self):
        if self.x < 0:
            return True
        return False

    # adds one if runner hits coin
    def collectCoin(self):
        self.score += 1

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
