import pygame
import os
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# caption of the game
pygame.display.set_caption('Journey to the west') 
# bg picture
setting_image = pygame.image.load("Desktop/final project/images/setting-bg.jpg")
music_icon = pygame.image.load("Desktop/final project/images/music.png")
m_on = pygame.image.load("Desktop/final project/images/on.png")
m_off = pygame.image.load("Desktop/final project/images/off.png")

musicon = True
def setting():
    screen.blit(setting_image , (0, 0))
    screen.blit(music_icon,(100,150))
    screen.blit(m_on,(100,300))
    screen.blit(m_off,(100,350))
    #start = icons(start_icon,400,500,130,64)
    rect1 = pygame.Rect(100,280,60,60)
    #setting = icons(set_icon,600,500,100,64)
    rect2 = pygame.Rect(100,350,80,80)
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #x , y = event.pos 
                if rect1.collidepoint(event.pos): 
                    musicon = True
                    running = False
                elif rect2.collidepoint(event.pos):
                    musicon = False
                    running = False
        pygame.display.update()
    return musicon
#setting()