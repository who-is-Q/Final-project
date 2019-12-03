import pygame
import os
WIN_WIDTH = 1000
WIN_HEIGHT = 600
 
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # the size of the window
pygame.display.set_caption("Journey to the West")  # caption of the window

class Player(object):
    def __init__(self, x, y, width, height,img, Tang):
        self.x = x
        self.y = y
        self.width = 65
        self.height = 110
        self.speed = 5
        self.left = False
        self.right = True
        self.isJump = False
        self.t = 10
        self.speed = 5
        self.img = img
        self.blood = 200
        self.who = Tang
        if self.who:
            self.blood_init = 200
            self.blood = 200
            self.range = 250
            self.attack = 30
        else:
            self.blood_init = 300
            self.blood = 300
            self.range = 150
            self.attack = 30
    def draw(self, win):
        if self.left:
            win.blit(self.img[1], (self.x, self.y))
        elif self.right:
            win.blit(self.img[0], (self.x, self.y))
        #self.hit_box = (self.x+40, self.y+40, 65, 110)
        #pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)
        # blood that are left
        #pygame.draw.rect(win, (0, 128, 0), (self.x + 40, self.y + 30, 40, 8))
        # blood that had been used
        #pygame.draw.rect(win, (255, 0, 0),(self.x + 40 - self.blood/self.blood_init, 
                                           #self.y + 30, 40 - self.blood/self.blood_init, 8))

def redraw():
    win.blit(bg, (0, 0)) 
    win.blit(boss1,(400, 410))
    player.draw(win)

#load pictures
pwalk_right = pygame.image.load('Desktop/final project/images/monk tang-r.png')
pwalk_left = pygame.image.load('Desktop/final project/images/monk tang-l.png')
pimg = [pwalk_right, pwalk_left]

#start_image = pygame.image.load("Desktop/final project/images/start-bg.jpg")

bg = pygame.image.load('Desktop/final project/images/bg1-2.jpg').convert() 
p_c1 = pygame.image.load('Desktop/final project/images/scene1/m6.jpg')
p_c2 = pygame.image.load('Desktop/final project/images/scene1/m7.jpg')
p_c3 = pygame.image.load('Desktop/final project/images/scene1/m8.jpg')
p_c4 = pygame.image.load('Desktop/final project/images/scene1/m9.jpg')
p_c5 = pygame.image.load('Desktop/final project/images/scene1/m10.jpg')
p = [p_c1, p_c2, p_c3, p_c4, p_c5]

boss1 = pygame.image.load('Desktop/final project/images/boss1-l.png')

player = Player(200, 410, 64, 64, pimg, Tang = True)

def scene4():
    rect = pygame.Rect(150,160,400,410)
    run = True
    talk = False
    clock = pygame.time.Clock()
    i = 0
    while run:
        clock.tick(60)
        redraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # the conversation picture
                if rect.collidepoint(event.pos): 
                    talk = True 
                i+=1
        if talk:
            if i<6:
                win.blit(p[i-1],(250,150))
            else:
                run = False
        #check the input from user
        keys = pygame.key.get_pressed()
        # a: go left
        # d: go right
        if keys[pygame.K_a] and player.x > 0:
            player.x -= player.speed
            player.left = True
            player.right = False
        elif keys[pygame.K_d] and player.x < win.get_size()[0] - player.width:
            player.x += player.speed
            player.left = False
            player.right = True
    
        # jump move of the player
        if not player.isJump:
            if keys[pygame.K_j]:
                player.isJump = True
        else:
            if player.t >= -10:
                if player.t < 0:
                    a = -1 
                else:
                    a = 1
                player.y -= 0.5 * a * (player.t ** 2)  # s = 0.5at^2
    
                player.t -= 1
            else:
                player.isJump = False
                player.t = 10
        pygame.display.update()