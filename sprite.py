import pygame
import random

pygame.mixer.init()
t1 = pygame.image.load("img/type1.png")
t2 = pygame.image.load("img/type2.png")
h = pygame.image.load("img/heart.png")
ss = pygame.image.load("img/blast.png")
shoot = pygame.mixer.Sound("msc/shoot.mp3")

class Spaceship:
    def __init__(self,x,y,w,h,img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.img = pygame.transform.scale(self.img,(self.w,self.h))
        self.movement = [False,False]
        self.rect = pygame.Rect(self.x,self.y,self.w-50,self.h-50)
        self.shoot = False
        self.temp = 1
        self.bullets = []

    def get(self):
        return self.img

    def update(self,x):
        self.rect = pygame.Rect(self.x,self.y,self.w-50,self.h-50)
        '''if(self.movement[0]) and (self.x > 0):
            self.x -= 5
        if(self.movement[1]) and (self.x < 1765):
            self.x += 5'''
        new_x = x - self.w / 2

        if self.shoot:
            self.temp += 1
            if(self.temp%5 == 0):
                self.bullets.append(Bullet(self.x+53,self.y-20))
                shoot.play()

        # Ensure the ship stays within the screen boundaries
        if new_x < 0:
            self.x = 0
        elif new_x > 1920 - self.w:
            self.x = 1920 - self.w
        else:
            self.x = new_x*3.2
        
        if self.x > 1770:
            self.x = 1770

class Spawner:
    def __init__(self,x,y,fact,type=1):
        self.health = 100
        self.x = x
        self.y = y
        self.type = type
        self.v = [0,0]
        self.rect = pygame.Rect(self.x,self.y,100,100)
        self.blast = False
        self.index = 1
        self.temp = 1

        if(type == 1):
            self.w = 70
            self.h = 70
            self.img = pygame.transform.scale(t1,(154,100))
            if(x < 0):
                self.v[0] = random.randint(1,10)
            else:
                self.v[0] = random.randint(-10,-1)
            self.v[1] = random.randint(-10,10)
        elif(type == 2):
            self.w = 100
            self.h = 100
            if(x < 0):
                self.v[0] = 7
                self.img = pygame.transform.scale(t2,(100,100))
                self.img = pygame.transform.rotate(self.img,-90)
            else:
                self.v[0] = -7
                self.img = pygame.transform.scale(t2,(100,100))
                self.img = pygame.transform.rotate(self.img,90)
    
    def get(self):
        return self.img
    
    def update(self):
        if not self.blast:
            self.x += self.v[0]
            self.y += self.v[1]
        if(self.health == 0):
            self.blast = True
        if(self.blast and self.index<6):
            self.image = ss
            if self.temp%3 == 0:
                self.index += 1
        self.rect = pygame.Rect(self.x,self.y,70,70)
            

class Health_bar:
    def __init__(self,win):
        self.win = win
        self.health = 100
        self.heart = pygame.transform.scale(h,(80,80))
    
    def reduce(self,n):
        self.health -= n
    
    def update(self):
        pygame.draw.rect(self.win,(255,255,0),(55,35,210,60))
        pygame.draw.rect(self.win,(255,0,0),(60,40,(self.health/100)*200,50))
        self.win.blit(self.heart,(20,20))

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 71
        self.h = 32
        self.render = True
        self.image = pygame.transform.rotate(pygame.image.load("img/bullet.png"),90)
    
    def update(self):
        self.y -= 20
        if(self.y > 1080):
            self.render = False
