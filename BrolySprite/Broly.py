import pygame
from pygame.locals import *
from time import sleep
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('Broly')

black=(0,0,0)

o=0
d=0
class character:
        def __init__(self,x,y):
                self.x=x
                self.y=y
                self.walklist=[]
                self.jumplist=[]
                self.throwlist=[]
                self.walk=0
                self.orbshoot=[]
                self.i=0
                self.walkcount=0
                self.jumpcount=0
                self.shoot=0
                self.direction=0
                self.shoot_direction=0
                self.jump=0
                self.jump_animation=0
                self.jump_check=0
                for i in range (0,7):
                        self.walklist.append(pygame.image.load('walk'+str(i)+'.png'))
                self.stand=pygame.image.load('stand.png')
                for e in range (0,2):
                        self.jumplist.append(pygame.image.load('jump'+str(e)+'.png'))
                for f in range (0,4):
                        self.throwlist.append(pygame.image.load('throw'+str(f)+'.png'))
                
        def update(self):
                if self.walk==0 and self.jump==0:
                        if self.direction==0:
                                screen.blit(self.stand,(self.x,self.y))
                        if self. direction==1:
                                screen.blit(pygame.transform.flip(self.stand,True,False),(self.x,self.y))
                if self.walk==1 and self.jump==0:
                        if self.direction==0:
                                screen.blit (self.walklist[self.i],(self.x,self.y))
                                self.x=self.x+5
                        if self.direction==1:
                                screen.blit(pygame.transform.flip(self.walklist[self.i],True,False),(self.x,self.y))
                                self.x=self.x-5
                        if self.walkcount==6:
                                self.i=self.i+1
                                if self.i>3:
                                        self.i=0
                        if self.walkcount==6:
                                self.walkcount=0
                        self.walkcount=self.walkcount+1
                if self.shoot==1:
                        self.orbshoot.append(orb(self.x,self.y,self.direction))
                        self.shoot=0
                for j in self.orbshoot:
                        if j.orb_direction==0:
                                screen.blit(j.image,(j.x,j.y))
                                j.x=j.x+4
                        if j.orb_direction==1:
                                screen.blit(pygame.transform.flip(j.image,True,False),(j.x,j.y))
                                j.x=j.x-4
                        if j.x > self.x+800:
                                self.orbshoot.remove(j)
                if self.jump==1:
                        if self.direction==0:
                                screen.blit(self.jumplist[self.jump_animation],(self.x,self.y))
                        if self.direction==1:
                                screen.blit(pygame.transform.flip(self.jumplist[self.jump_animation],True,False),(self.x,self.y))
                        if self.jumpcount==8:
                                self.jump_animation=self.jump_animation+1
                                if self.jump_animation ==2:
                                        self.jump_animation=0
                                        self.jump_check=1
                                if self.jump_check==1 and self.jump_animation==1:
                                        self.jump_animation=0
                                        self.jump_check=0
                                        self.jump=0
                        if self.jumpcount==8:
                                self.jumpcount=0
                        self.jumpcount=self.jumpcount+1
class orb:
        def __init__(self,x,y,orb_direction):
                self.x=x
                self.y=y
                self.orb_direction=orb_direction
                self.image=pygame.image.load('orb1.png')


clock=pygame.time.Clock()
c=character(100,100)
while True:
        clock.tick(60)
        pygame.display.update()
        screen.fill(black)
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.quit()
                        exit()
                if event.type==KEYDOWN:
                        if event.key==K_SPACE:
                                c.shoot=1
                        if event.key==K_d:
                                c.walk=1
                                c.direction=0
                        if event.key==K_a:
                                c.walk=1
                                c.direction=1
                        if event.key==K_w:
                                c.jump=1
                if event.type==KEYUP:
                        if event.key==K_d:
                                c.walk=0
                        if event.key==K_a:
                                c.walk=0
        c.update()
