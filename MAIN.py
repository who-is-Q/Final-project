import pygame
from sys import exit
from pygame.locals import *
import random
import math

g = 0.3
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_x, init_pos,distance,fc,attack):
        pygame.sprite.Sprite.__init__(self)
        if fc == "left":
            self.image = bullet_img[0]
        else:
            self.image = bullet_img[1]
        self.ini = init_x
        self.rect = self.image.get_rect()
        self.rect.center = init_pos          # Initialize the position of the bullet
        self.speed = 10 
        self.attack = attack                 # how many harm can this character cause
        self.direction = fc
        self.d = distance
    def move(self):
        # if fly out of range, kill the bullet
        alive = True
        while alive == True:
            if (self.rect.x-self.ini)>self.d:
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
                    self.rect.x += self.speed
    

class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, player_rect, init_pos, blood, magic, distance, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.face = "right"
        self.i = player_img
        self.image = player_img[1]
        self.rect = player_rect                      # 初始化图片所在的矩形
        self.rect.midtop = init_pos                    
        self.speed = 8                                  
        self.bullets = pygame.sprite.Group()                                         
        self.is_hit = False                             
        self.onground = True
        self.blood = blood
        self.magic = magic
        self.level = 1
        self.bullet_img = bullet_img
        self.distance = distance
        self.attack = 50

    def shoot(self):
        bullet = Bullet(self.bullet_img, self.rect.x, self.rect.center, 30, self.face, self.attack)
        self.bullets.add(bullet)
    # 向上移动，需要判断边界
    def moveUp(self):
        #if self.rect.y <= 0:
        #    self.rect.y = 0
        #else:
            self.rect -= self.speed
    # 向左移动，需要判断边界
    def moveLeft(self):
        if self.face == "right":
            self.face = "left"
            self.image = self.i[0]
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed 
    # 向右移动，需要判断边界        
    def moveRight(self):
        if self.face == "left":
            self.face = "right"
            self.image = self.i[1]
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, init_pos,blood,distance,attack,bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.face = "right"
        self.i = enemy_img
        self.image = enemy_img[1]
        self.rect = self.image.get_rect()
        self.rect.midtop = init_pos
        self.speed = 2
        self.down_index = 0
        self.onground = True
        self.blood = blood
        self.bullet_img = bullet_img
        self.distance = distance
        self.attack = attack
        self.bullets = pygame.sprite.Group()
    # 发射子弹
    def shoot(self):
        bullet = Bullet(self.bullet_img, self.rect.x, self.rect.center,self.distance,self.face,self.attack)
        self.bullets.add(bullet)
    # 向上移动，需要判断边界
    def moveUp(self):
        if self.rect.midtop <= 0:
            self.rect.midtop = 0
        else:
            self.rect.mid
            top -= self.speed
    # 向下移动，需要判断边界
    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed 
    # 向左移动，需要判断边界
    def moveLeft(self):
        if self.face == "right":
            self.face = "left"
            self.image = self.i[0]
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed 
    # 向右移动，需要判断边界        
    def moveRight(self):
        if self.face == "left":
            self.face = "right"
            self.image = self.i[1]
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed
 

pygame.init() 
# the size of the user interface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
# caption of the game
pygame.display.set_caption('Journey to the west') 
# bg picture
background = pygame.image.load('Desktop/final project/images/bg1-1.jpg').convert() 
# symbol of fail
# load pictuers
player_img1 = pygame.image.load('Desktop/final project/images/monk tang-l.png')
player_img2 = pygame.image.load('Desktop/final project/images/monk tang-r.png')
player_img = [player_img1,player_img2] 
pbullet_img1 = pygame.image.load('Desktop/final project/images/mt-k-left.png')
pbullet_img2 = pygame.image.load('Desktop/final project/images/mt-k-right.png')
pbullet_img = [pbullet_img1,pbullet_img2]
player = Player(player_img,Rect(100,20,10,10),(SCREEN_WIDTH-200,SCREEN_HEIGHT-200),blood=200, magic = 200, distance = 30, bullet_img = pbullet_img )
me = pygame.sprite.Group()
me.add(player)
# initialized the shoot, and the number of enemies
enemy_img1 = pygame.image.load('Desktop/final project/images/enemy-l.png')
enemy_img2 = pygame.image.load('Desktop/final project/images/enemy-r.png')
enemy_img = [enemy_img1,enemy_img2]
ebullet_img1 = pygame.image.load('Desktop/final project/images/enemy-k-left.png')
ebullet_img2 = pygame.image.load('Desktop/final project/images/enemy-k-right.png')
ebullet_img = [ebullet_img1,ebullet_img2]
shoot_frequency = 0
enemy_index = 0
#initialize the group of enemies
enemies = pygame.sprite.Group()
#control the minutes that is used to control the the renew
clock = pygame.time.Clock()
# judge if it is running
running = True

pygame.mixer.init()
pygame.mixer.music.load("Desktop/final project/jianghu.mp3")
pygame.mixer.music.play()

# main loop
while running:
    clock.tick(60) 
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_j] and player.onground:
        player.moveUp()
        player.onground = False
    if key_pressed[K_a]:
        player.moveLeft()
    if key_pressed[K_d]:
        player.moveRight()
    if key_pressed[K_k]:
        player.shoot()
    if not player.onground:
        if (player.rect.y+g) < (SCREEN_HEIGHT-200):
            player.rect.y += g
        else:
            player.rect.y == (SCREEN_HEIGHT-200)
            player.onground = True
    # produce bullets
    # judge if the the play is hit
    if not player.is_hit:
        if shoot_frequency % 60 == 0:
            player.shoot()
        shoot_frequency += 1
        if shoot_frequency >= 60:
            shoot_frequency = 0 
    # form enemies, control the numver of enermy
    while enemy_index < 10 :
        enemy1_pos = [random.randint(0, SCREEN_WIDTH-100), SCREEN_HEIGHT-200]
        enemy1 = Enemy(enemy_img,enemy1_pos, 100, 10, 10, ebullet_img)
        enemies.add(enemy1)
        enemy_index += 1  
    for enemy in enemies:
        if player.rect.x-enemy.rect.x <= enemy.distance:
            enemy.face = "right"
            enemy.shoot()
        if player.rect.x < enemy.rect.x:
            enemy.moveLeft()
        if player.rect.x > enemy.rect.x:
            enemy.moveRight()
    # if enemy is taken down, delete the sprite
    for e in enemies:
        for b in player.bullets:
            if pygame.sprite.collide_rect(e, b):
                e.blood-=b.attack
            if e.blood <= 0:
                enemies.remove(enemy)
    # draw the background
    screen.fill(0)
    screen.blit(background, (0, 0))
    # draw the player
    screen.blit(player.image, player.rect)
    if player.blood <= 0:
        running = False
    # show bullets
    for i in player.bullets:
        i.move()
        player.bullets.update()
    player.bullets.draw(screen)
    # show enemies
    enemies.draw(screen)
    for i in enemies:
        for j in i.bullets:
            j.move()
            i.bullets.update()
    player.bullets.draw(screen)
    # renew the screen
    pygame.display.update() 
    # exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()