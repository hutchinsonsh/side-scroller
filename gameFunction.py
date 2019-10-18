import pygame
import sys


def updateScreen(ai_settings, screen, runner, objects, coins, sb):
    # makes mouse invisible if the game is being played
    if ai_settings.gameActive:
        pygame.mouse.set_visible(False)
    emptyList = False
    screen.blit(ai_settings.bg, (ai_settings.bgX, 0))
    screen.blit(ai_settings.bg, (ai_settings.bgX2, 0))
    runner.draw(screen)

    # checks to see if runner hits any vines or logs; also moves vines and logs with rolling screen
    for x in objects:
        if x.collide(runner.hitbox):
            runner.falling = True
            if ai_settings.pause == 0:
                ai_settings.setFallSpeed(ai_settings.getSpeed())
                ai_settings.setPause(1)
        x.x -= 1.4
        if x.x < x.width * -1:
            objects.pop(objects.index(x))
    # draws updated objects
    for x in objects:
        x.draw(screen)
    # checks to see if runner hits any coins; moves coins and removes coins if hit and updates coinsCollected
    for x in coins:
        if x.collide(runner.hitbox):
            coins.remove(x)
            sb.collectCoin()
        x.x -= 1.4
    # draws updated coins; deletes coins that are out of frame
    for x in coins:
        #if x.update() == True:
            #coins.remove(x)
        x.draw(screen)

    # updates and prints out score/coinsCollected
    sb.updateScore()
    sb.updateScreen()

    # for if user hits object
    if ai_settings.pause > 0:
        ai_settings.addPause()
        if ai_settings.pause > 200:
            endScreen(ai_settings, screen, runner, sb)
            ai_settings.initDynamicSettings()
            emptyList = True

    # displays update on list; if end screen is being shown- returns true if game over
    pygame.display.update()
    return emptyList


# for end screen
def endScreen(ai_settings, screen, runner, sb):
    run = True
    while run:
        # waits 1 sec before endscreen shown- sets mouse visible again
        pygame.time.delay(1000)
        pygame.mouse.set_visible(True)
        # waits until user either exits game or presses screen to restart game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                runner.centerRunner()
        # displays highest score and current score
        screen.blit(ai_settings.bg, (0, 0))
        largeFont = pygame.font.SysFont("comicsans", 80)
        previousScore = largeFont.render("High Score: " + str(updateFile(sb)), 1, (0, 0, 0))
        newScore = largeFont.render("Current Score: " + str(sb.getScore()), 1, (0, 0, 0))
        screen.blit(previousScore, (ai_settings.W/2 - previousScore.get_width()/2, 200))
        screen.blit(newScore, (ai_settings.W / 2 - newScore.get_width() / 2, 320))
        pygame.display.update()
    # resets stats
    sb.resetGame()
    ai_settings.gameActive = True


# replaces highest score if beaten
def updateFile(sb):
    f = open('scoreText', 'r')
    file = f.readlines()
    last = int(file[0])
    if last < int(sb.getScore()):
        f.close()
        file = open('scoreText', 'w')
        file.write(str(sb.getScore()))
        return sb.getScore()
    return last


# checks if user presses up/down arrow; checks user buttons
def checkEvents(runner, settings):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if not(runner.jumping):
            runner.jumping = True;
    if keys[pygame.K_DOWN]:
        if not(runner.sliding):
            runner.sliding = True;
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            checkKeyDown(event, settings)


# pause button(P) and quit button (Q)
def checkKeyDown(event, settings):
    if event.key == pygame.K_p and settings.gameActive == True:
        settings.gameActive = False
        pygame.mouse.set_visible(True)
    elif event.key == pygame.K_p and settings.gameActive == False:
        settings.gameActive = True
        pygame.mouse.set_visible(False)
    elif event.key == pygame.K_q:
        sys.exit()
        
