import pygame
from pygame.locals import *
import random
import gameFunction as gf
from runner import Runner
from log import Log
from vine import Vine
from coin import Coin
from settings import Settings
from pygame.sprite import Group
from scoreboard import Scoreboard

pygame.init()
ai_settings = Settings()
ai_settings.initDynamicSettings()
pygame.display.set_caption('Side Scroller')
screen = pygame.display.set_mode((ai_settings.W, ai_settings.H))
sb = Scoreboard(ai_settings, screen)

clock = pygame.time.Clock()

runner = Runner(400, 300, 75, 75)
# for increasing speed, setting up obstacles, setting up coins respectively
pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, random.randrange(3000, 5000))
pygame.time.set_timer(USEREVENT+3, 3000)
run = True
objects = []
coins = Group()


while run:
    gf.checkEvents(runner, ai_settings)
    if ai_settings.gameActive:
        emptyObj = gf.updateScreen(ai_settings, screen, runner, objects, coins, sb)
        # for emptying the coins and obstacles if runner hits obstacle
        if emptyObj == True:
            objects = []
            for x in coins:
                coins.remove(x)

        # for creating obstacles, coins, and increases speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == USEREVENT+1:
                ai_settings.increaseSpeed()
            if event.type == USEREVENT+2:
                r = random.randrange(0, 2)
                if r == 0:
                    log = Log(810, 310, 100, 100)
                    objects.append(log)
                elif r == 1:
                    vine = Vine(810, 0, 60, 300)
                    objects.append(vine)
            if event.type == USEREVENT+3:
                # for making sure that the coins are placed above the logs when first spawned
                if len(objects) > 0 and 700 < objects[len(objects)-1].x < 900 and objects[len(objects)-1].y == 310:
                    new_coin = Coin(810, 210, 100, 100)
                    coins.add(new_coin)
                else:
                     new_coin = Coin(810, 310, 100, 100)
                     coins.add(new_coin)

        clock.tick(ai_settings.speed)
        ai_settings.rollingScreen()
