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
# bg picture

class icons():
    def __init__(self, img,x,y,width,height):
        self.image = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self):
        screen.blit(self.image,(self.x,self.y))

strt = True
def start():
    start_image = pygame.image.load("Desktop/final project/images/start-bg.jpg")
    screen.blit(start_image, (0, 0))
    
    start_icon = pygame.image.load("Desktop/final project/images/start.png")
    set_icon = pygame.image.load("Desktop/final project/images/set.png")
   
    start = icons(start_icon,400,500,130,64)
    rect1 = pygame.Rect(400,500,130,64)
    setting = icons(set_icon,600,500,100,64)
    rect2 = pygame.Rect(600,500,100,64)
    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(60)
        start.draw()
        setting.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #x , y = event.pos 
                if rect1.collidepoint(event.pos): 
                    strt = True
                    running = False
                elif rect2.collidepoint(event.pos):
                    strt = False
                    running = False
                    
        pygame.display.update()