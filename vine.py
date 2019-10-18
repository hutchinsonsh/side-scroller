import pygame
import os

class Vine(object):
    img = pygame.image.load(os.path.join('images', 'vine.png'))

    def __init__(self, x, y, width, height):
        super(Vine, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)

    # checks to see collision
    def collide(self, rect):
        if(rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]):
            if rect[1] + 10 < self.hitbox[3]:
                return True
        return False

    def draw(self, win):
        self.hitbox = (self.x + 40, self.y, 28, 315)
        win.blit(self.img, (self.x, self.y))
