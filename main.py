
#opencv
import cv2
import mediapipe as mp
import pyautogui

import random
import pygame
from pygame import mixer
from sprite import Spaceship,Spawner,Health_bar

pygame.init()

pygame.display.set_caption("HESTIA 24")
win = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)

spc = pygame.image.load("img/spaceship.png").convert_alpha()
bg = pygame.image.load("img/bg.jpg").convert()
bgm = mixer.music.load("msc/bgm.mp3")
game_over_font = pygame.font.SysFont('Verdana', 60)
mixer.music.play(-1)

clock = pygame.time.Clock()

#opencv
mp_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

class Gameover:
    def __init__(self,score):
        self.score = score
        self.text = game_over_font.render("Game Over", True, (255,0,0))
        self.run = True
    def update(self):
        win.blit(self.text, (100,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

        pygame.display.update()
        

class Game:
    def __init__(self):
        self.run = True
        
        self.ship = Spaceship(860,900,150,150,spc)
        self.s1 = Spawner(-200,500,0.5,2)
        self.s2 = Spawner(1000,100,0.5,2)
        self.s3 = Spawner(1000,300,0.5,2)
        self.s4 = Spawner(-200,300,0.5,2)
        self.hb = Health_bar(win)
        self.hb.health = 10

    def update(self):
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = mp_hands.process(frame_rgb)
        #print("Number of hands detected:", len(results.multi_hand_landmarks))
        if results.multi_hand_landmarks is not None:
            print("Number of hands detected:", len(results.multi_hand_landmarks))
            for hand_landmarks in results.multi_hand_landmarks:
                x = int(hand_landmarks.landmark[0].x * frame.shape[1])

                x_p = int(hand_landmarks.landmark[8].x * frame.shape[1])
                y_p = int(hand_landmarks.landmark[8].y * frame.shape[0])

                x_t = int(hand_landmarks.landmark[4].x * frame.shape[1])
                y_t = int(hand_landmarks.landmark[4].y * frame.shape[0])

                dist = ((x_t - x_p) * 2 + (y_t - y_p)*2) * 0.5 // 4
                self.ship.update(x)
                if dist < 10:
                    self.ship.shoot = True
                else:
                    self.ship.shoot = False
        else:
            print("No hands detected.")
        #cv2.imshow("Hand volume control", frame)
        clock.tick(60)
        win.blit(bg,(0,0))
        win.blit(self.ship.get(),(self.ship.x,self.ship.y))
        win.blit(self.s1.get(),(self.s1.x,self.s1.y))
        win.blit(self.s2.get(),(self.s2.x,self.s2.y))
        win.blit(self.s3.get(),(self.s3.x,self.s3.y))
        win.blit(self.s4.get(),(self.s4.x,self.s4.y))

        #self.ship.update()
        #healtself.hbar
        self.hb.update()

        #Spawner move
        self.s1.update()
        self.s2.update()
        self.s3.update()
        self.s4.update()
        
        if((self.s1.x > 1980 or self.s1.x < -200) or (self.s1.y > 1200 or self.s1.y < -100)) or self.s1.health == 0:
            tp = random.randint(1,2)
            if(tp == 1):
                self.s1 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
            elif(tp == 2):
                self.s1 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
        
        if((self.s2.x > 1980 or self.s2.x < -200) or (self.s2.y > 1200 or self.s2.y < -100)) or self.s2.health == 0:
            tp = random.randint(1,2)
            if(tp == 1): 
                self.s2 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
            elif(tp == 2):
                self.s2 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
        
        if((self.s3.x > 1980 or self.s3.x < -200) or (self.s3.y > 1200 or self.s3.y < -100)) or self.s3.health == 0:
            tp = random.randint(1,2)
            if(tp == 1):
                self.s3 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
            elif(tp == 2):
                self.s3 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)

        if((self.s4.x > 1980 or self.s4.x < -200) or (self.s4.y > 1200 or self.s4.y < -100)) or self.s4.health == 0:
            tp = random.randint(1,2)
            if(tp == 1):
                self.s4 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
            elif(tp == 2):
                self.s4 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
        
        if(pygame.Rect.colliderect(self.ship.rect,self.s1.rect)):
            self.hb.reduce(10)
            tp = random.randint(1,2)
            if(tp == 1):
                self.s1 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
            elif(tp == 2):
                self.s1 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
        if(pygame.Rect.colliderect(self.ship.rect,self.s2.rect)):
            self.hb.reduce(10)
            tp = random.randint(1,2)
            if(tp == 1):
                self.s2 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
            elif(tp == 2):
                self.s2 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
        if(pygame.Rect.colliderect(self.ship.rect,self.s3.rect)):
            self.hb.reduce(10)
            tp = random.randint(1,2)
            if(tp == 1):
                self.s3 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
            elif(tp == 2):
                self.s3 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
        if(pygame.Rect.colliderect(self.ship.rect,self.s4.rect)):
            self.hb.reduce(10)
            tp = random.randint(1,2)
            if(tp == 1):
                self.s4 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
            elif(tp == 2):
                self.s4 = Spawner(random.sample([-150,1920],1)[0],random.randint(100,400),0.5,tp)
        i = 0
        while i < len(self.ship.bullets):
            if self.ship.bullets[i].render:
                self.ship.bullets[i].update()
                win.blit(self.ship.bullets[i].image, (self.ship.bullets[i].x, self.ship.bullets[i].y))                 
            else:
                self.ship.bullets.pop(i)
                continue  # Skip the rest of the loop for this iteration
            if (self.s1.x < self.ship.bullets[i].x < self.s1.x + self.s1.w) and (self.s1.y < self.ship.bullets[i].y < self.s1.y + self.s1.h):
                self.s1.health -= 50
                self.ship.bullets[i].render = False# Move to the next bullet
                #break
            if (self.s2.x < self.ship.bullets[i].x < self.s2.x + self.s2.w) and (self.s2.y < self.ship.bullets[i].y < self.s2.y + self.s2.h):
                self.s2.health -= 50
                self.ship.bullets[i].render = False
                #break
            if (self.s3.x < self.ship.bullets[i].x < self.s3.x + self.s3.w) and (self.s3.y < self.ship.bullets[i].y < self.s3.y + self.s3.h):
                self.s3.health -= 50
                self.ship.bullets[i].render = False
                #break
            if (self.s4.x < self.ship.bullets[i].x < self.s4.x + self.s4.w) and (self.s4.y < self.ship.bullets[i].y < self.s4.y + self.s4.h):
                self.s4.health -= 50
                self.ship.bullets[i].render = False
            i+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                    self.ship.movement[0] = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.ship.movement[1] = True
                if event.key == pygame.K_SPACE:
                    self.ship.shoot = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.ship.movement[0] = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.ship.movement[1] = False
                if event.key == pygame.K_SPACE:
                    self.ship.shoot = False

        pygame.display.update()
        global game
        if(self.hb.health == 0):
            game = Gameover(100)

game = Game()

while game.run:
    game.update()