import pygame
import os
import random
pygame.init()
 
WIN_WIDTH = 1000
WIN_HEIGHT = 600
 
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # the size of the window
pygame.display.set_caption("Journey to the West")  # caption of the window

# bullets
class Bullet(object):
    def __init__(self, x, y, radius, color, facing, img, range):
        self.init_x = x
        self.range = range
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.img = img
        self.width = 60
        self.height = 45
        self.attack = 0
    def draw(self, win):
        # according to the direction of the character, switch image
        if self.facing == -1:
            win.blit(self.img[1], (self.x, self.y))
        else:
            win.blit(self.img[0], (self.x, self.y))
        self.hit_box = (self.x+25, self.y+8, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)
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
        self.blood = 1000
        self.who = Tang
        if self.who:
            self.blood_init = 1000
            self.blood = 1000
            self.range = 250
            self.attack = 30
        else:
            self.blood_init = 1300
            self.blood = 1300
            self.range = 150
            self.attack = 30
    def draw(self, win):
        if self.left:
            win.blit(self.img[1], (self.x, self.y))
        elif self.right:
            win.blit(self.img[0], (self.x, self.y))
        self.hit_box = (self.x+40, self.y+40, 65, 110)
        #pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)
        # blood that are left
        pygame.draw.rect(win, (0, 128, 0), (self.x + 40, self.y , 40, 8))
        # blood that had been used
        pygame.draw.rect(win, (255, 0, 0),(self.x + 40 + self.blood/self.blood_init*40, 
                                           self.y , 40 - 40*self.blood/self.blood_init, 8))
class Monster(object):
    def __init__(self, x, y, width, height,img):
        self.x = x
        self.y = y
        self.width = 65
        self.height = 110
        self.speed = 5
        self.left = False
        self.right = True
        # self.isJump = False
        self.t = 10
        self.speed = 1
        self.img = img
        self.blood = 200
        self.range = 50
        self.attack = 10
    def draw(self, win):
        if self.left:
            win.blit(self.img[1], (self.x, self.y))
        elif self.right:
            win.blit(self.img[0], (self.x, self.y))
        self.hit_box = (self.x+40, self.y+40, 65, 110)
        #pygame.draw.rect(win, (255, 0, 0), self.hit_box, 2)
        pygame.draw.rect(win, (0, 128, 0), (self.x + 40, self.y , 40, 8))
        # blood that had been used
        pygame.draw.rect(win, (255, 0, 0),(self.x + 40 + self.blood/50000*40, 
                                           self.y , 40 - 40*self.blood/50000, 8))
def collision_check(a, b):
    temp1 = (b.x <= a.x + a.width <= b.x + b.width)
    temp2 = (b.y <= a.y + a.height <= b.y + b.height)
    return (temp1 and temp2)

def redraw():
    win.blit(bg, (0, 0)) 
    player.draw(win)
    for bullet in pbullets:
        bullet.draw(win)
    for bullet in plbullets:
        bullet.draw(win)
    boss.draw(win)
    for b in mbullets:
        b.draw(win)
    pygame.display.update()

bg = pygame.image.load('Desktop/final project/images/bg1-2.jpg').convert() 
#char = pygame.image.load(img_base_path + 'standing.png')
# load pictures for player
pbullet_left = pygame.image.load('Desktop/final project/images/mt-k-left.png')
pbullet_right = pygame.image.load('Desktop/final project/images/mt-k-right.png')
pbullet_img = [pbullet_right,pbullet_left]
pbulletl_left = pygame.image.load('Desktop/final project/images/mt-l-l.png')
pbulletl_right = pygame.image.load('Desktop/final project/images/mt-l-l.png')
pbulletl_img = [pbulletl_right,pbulletl_left]
pwalk_right = pygame.image.load('Desktop/final project/images/monk tang-r.png')
pwalk_left = pygame.image.load('Desktop/final project/images/monk tang-l.png')
pimg = [pwalk_right, pwalk_left]
# load pictures for monsters
mbullet_left = pygame.image.load('Desktop/final project/images/enemy-k-left.png')
mbullet_right = pygame.image.load('Desktop/final project/images/enemy-k-right.png')
mbullet_img = [mbullet_left,mbullet_right]
monster_left = pygame.image.load('Desktop/final project/images/boss1-l.png')
monster_right = pygame.image.load('Desktop/final project/images/boss1-r.png')
mimg = [monster_right,monster_left]

plbullets = []
pbullets = []

mbullets = []
player = Player(200, 410, 64, 64, pimg, Tang = True)
boss = Monster(400,410,64,64,mimg)
boss.blood = 50000
# main
def fight2():
    run = True
    clock = pygame.time.Clock()
    monster_index = 0
    player.blood = player.blood_init
    end = 1
    rect = pygame.Rect(300,125,50,50)
    while run:
        clock.tick(48)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    end = 2
                    run = False
        # player within the range of attack, attack the player
        if player.x - boss.x <= boss.range:
            boss.left = False
            boss.right = True
        else:
            boss.left = True
            boss.right = False
        if len(pbullets) < 6: 
            # there could only be six bullets on the screen
            # if press k when there has been already five, do not add anything
            if boss.left:
                facing = -1
            else:
                facing = 1
            bullet = Bullet(round(boss.x + boss.width // 2), round(boss.y + boss.height // 2), 6, (0, 0, 0), facing, mbullet_img,boss.range)
            mbullets.append(bullet)
            # player at the left side, move to the left
        if player.x < boss.x:
            boss.x -= boss.speed
            boss.left = True
            boss.right = False
        # player at the right side, move to the right
        if player.x > boss.x:
            boss.x += boss.speed
            boss.left = False
            boss.right = True
        # check bullets of monsters whether out of range
        for bullet in mbullets:
            if WIN_WIDTH > bullet.x > 0 and bullet.range >= abs(bullet.init_x - bullet.x):
                bullet.x += bullet.vel
            else:
                mbullets.pop(mbullets.index(bullet))
        # check bullets of player whether it is out of range
        for bullet in pbullets:
            if WIN_WIDTH > bullet.x > 0 and bullet.range >= abs(bullet.init_x - bullet.x):
                bullet.x += bullet.vel
            else:
                pbullets.pop(pbullets.index(bullet))
        for bullet in plbullets:
            if WIN_WIDTH > bullet.x > 0 and bullet.range >= abs(bullet.init_x - bullet.x):
                bullet.x += bullet.vel
            else:
                plbullets.pop(plbullets.index(bullet))
        # check if there is collision between player's bullets
        # and the monsters
        # if there is, decrease the monster's blood
        for p in pbullets:
            if collision_check(p, boss) or collision_check(boss, p):
                boss.blood -= player.attack
                if boss.blood < 0:
                    end = 1
                    run = False
        for pl in plbullets:
            if collision_check(pl, boss) or collision_check(boss, pl):
                boss.blood -= boss.attack
                if boss.blood < 0:
                    end = 1
                    run = False
        # check if there is collision between monster's bullets and player
        # if there is, decrease the player's blood
        for m in mbullets:
            if collision_check(player, m) or collision_check(m, player):
                    player.blood -= boss.attack
                    if player.blood < 0:
                        player.blood = 0
                        #run = False
                        pass

        #check the input from user
        keys = pygame.key.get_pressed()
        # k: attack
        # a: go left
        # d: go right
        if keys[pygame.K_k]:
            if len(pbullets) < 6: 
                # there could only be five bullets on the screen
                # if press k when there has been already five, do not add anything
                if player.left:
                    facing = -1
                else:
                    facing = 1
                bullet = Bullet(round(player.x + player.width // 2), round(player.y + player.height // 2), 6, (0, 0, 0), facing, pbullet_img, player.range)
                pbullets.append(bullet)
        if keys[pygame.K_l]:
            if len(plbullets) < 2: 
                # there could only be five bullets on the screen
                # if press k when there has been already five, do not add anything
                if player.left:
                    facing = -1
                else:
                    facing = 1
                bullet = Bullet(round(player.x + player.width // 2), round(player.y + player.height // 2), 6, (0, 0, 0), facing, pbulletl_img, 350)
                bullet.attack = 60
                plbullets.append(bullet)
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
                player.walkCount = 0
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
        redraw()
    return end