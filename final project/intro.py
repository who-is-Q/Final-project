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
intro_image = pygame.image.load("Desktop/final project/images/intro.jpg")

def intro():
    run = True
    while run:
        screen.blit(intro_image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            run = False