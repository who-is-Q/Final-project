import pygame
from sys import exit
from pygame.locals import *
import random
import math

g = 0.3
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_x, init_center,distance,fc,attack):
        pygame.sprite.Sprite.__init__(self)
        if fc == "left":
            self.image = bullet_img[0]
        else:
            self.image = bullet_img[1]
        self.rect = self.image.get_rect()
        #self.rect.x = init_x
        #self.rect.top = init_top         # Initialize the position of the bullet
        #self.rect = ((init_x, init_y))
        self.rect.center = init_center
        self.init_x = init_x
        self.speed = 10 
        self.attack = attack                 # how many harm can this character cauaaaaa    self.direction = fc
        self.d = distance
        self.direction = fc
    '''def move(self):
        # if fly out of range, kill the bullet
        alive = True
        while alive == True:
            if abs(self.rect.x-self.init_x)>self.d:
                self.kill()
                alive = False
            # if fly out of screen, kill the bullet
            elif (self.rect.x<0) or (self.rect.x>SCREEN_WIDTH):
                self.kill()
                alive = False
            else:
                # if the player shoot facing left, the bullet should fly to the left
                if self.direction == "left":
                    self.rect.x -= self.speed
                # if the player shoot facing right, the bullet should fly to the right
                else:
                    self.rect.x += self.speed'''
    #def draw(self, win):
    #    # 根据人物的朝向，要切换不同的子弹图片
    #    win.blit(bullet_left, (self.x, self.y))
    

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, player_rect, init_pos, blood, magic, distance, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.face = "right"
        self.i = player_img
        self.image = player_img[1]
        self.rect = player_rect                      # 初始化图片所在的矩形
        self.rect.midtop = (init_pos[0],init_pos[1])
        self.init_y = init_pos[0]
        self.speed = 8                                  
        self.bullets = pygame.sprite.Group()                                         
        self.is_hit = False                             
        self.onground = True
        self.blood = blood
        #self.magic = magic
        self.bullet_img = bullet_img
        self.distance = distance
        self.attack = 50 
        self.t = 10
    def shoot(self):
        bullet = Bullet(self.bullet_img, self.rect.x, self.rect.center, 30, self.face, self.attack)
        self.bullets.add(bullet)
    # jump
    def moveUp(self):
        if self.t >= -10:
            a = 1  # first half go upward
            if self.t < 0:
                a = -1  # last half go downward
            self.rect.y -= 0.5 * a * (self.t ** 2)  # s = 0.5at^2
            self.t -= 1
        else:
            self.onground = True
            self.t = 10
    # move to the left
    def moveLeft(self):
        if self.face == "right":
            self.face = "left"
            self.image = self.i[0]
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed 
    # move to the right        
    def moveRight(self):
        if self.face == "left":
            self.face = "right"
            self.image = self.i[1]
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed
