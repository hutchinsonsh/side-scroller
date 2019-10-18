import pygame
import os

class Log(object):
    img = pygame.image.load(os.path.join('images', 'log.png'))

    def __init__(self, x, y, width, height):
        super(Log, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)

    # checks to see collision
    def collide(self, rect):
        if(rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]):
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

    def draw(self, win):
        self.hitbox = (self.x+ 10, self.y + 30, self.width- 30, self.height - 30)
        win.blit(pygame.transform.scale(self.img,(100, 100)),(self.x, self.y))
        
