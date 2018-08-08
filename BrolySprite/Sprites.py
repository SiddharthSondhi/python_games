import pygame
from pygame.locals import *
from time import sleep
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('Sprites!!')

black=(0,0,0)
img=[]
jump=[]
throw=[]
orb=[]
for i in range (0,7):
        img.append(pygame.image.load('walk'+str(i)+'.png'))
for e in range (0,2):
        jump.append(pygame.image.load('jump'+str(e)+'.png'))
        orb.append(pygame.image.load('orb'+str(e)+'.png'))
for f in range (0,4):
        throw.append(pygame.image.load('throw'+str(f)+'.png'))
stand=pygame.image.load('stand.png')
i=0
c=pygame.time.Clock()
x=100
y=100
walk=0
j=0
ju=0
jmp=0
s=0
t=0
orbblit=0
orbx=85
while True:
        c.tick(7.5)
        pygame.display.update()
        screen.fill(black)
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.quit()
                        exit()
                if event.type==KEYDOWN:
                        if event.key == K_d:
                                walk=1
                        if event.key == K_w:
                                j=1
                        if event.key == K_SPACE:
                                s=1
                if event.type==KEYUP:
                        if event.key == K_d:
                                walk=0
        if walk ==1 and j==0:                
                x=x+9
                screen.blit (img[i],(x,y))
                i=i+1
                if i>4:
                        i=0
        elif j ==1:
                screen.blit(jump[ju],(x,y))
                ju=ju+1
                if ju ==2:
                        ju=0
                        jmp=1
                if jmp==1 and ju==1:
                        ju=0
                        jmp=0
                        j=0
        elif s ==1:
                screen.blit(throw[t],(x,y))
                if t==3:
                        orbblit=1
                t=t+1
                if t>3:
                        t=0
                        s=0
        else:
                screen.blit (stand,(x,y))

        if orbblit ==1:
                screen.blit(orb[1],(x+orbx,y+20))
                orbx=orbx+20

                                        

