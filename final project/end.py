import pygame
import os
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
img_base_path = "./images/"
#start_image = pygame.image.load("Desktop/final project/images/start-bg.jpg")


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# caption of the game
pygame.display.set_caption('Journey to the west') 
end_image = pygame.image.load("Desktop/final project/images/end.jpg")

def end():
    run = True
    while run:
        screen.blit(end_image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()