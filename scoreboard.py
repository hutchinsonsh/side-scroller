import pygame
class Scoreboard():
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.font = pygame.font.SysFont('comicsans', 30)
        self.score = 0
        self.coinCollect = 0

    def collectCoin(self):
        self.coinCollect += 1

    def updateScore(self):
        self.score = self.ai_settings.getSpeed() // 5 - 6

    def getScore(self):
        return self.score

    def getCoin(self):
        return self.coinCollect

    def resetGame(self):
        self.coinCollect = 0
        self.score = 0

    def updateScreen(self):
        self.text = self.font.render("Score: " + str(self.getScore()), 1, (255, 255, 255))
        self.text2 = self.font.render("Coins: " + str(self.getCoin()), 1, (255, 255, 255))
        self.screen.blit(self.text, (700, 50))
        self.screen.blit(self.text2, (700, 100))
        
        
