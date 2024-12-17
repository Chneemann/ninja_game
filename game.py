import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("ninja game")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        
        self.img = pygame.image.load("data/images/entities/player/idle/00.png")
        self.img.set_colorkey((0, 0, 0))
        
        self.img_pos = [160, 260]

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            
            self.screen.blit(self.img, self.img_pos)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()