import pygame
from time import sleep
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
blue=(8,160,125)
white=(155,169,55)
black=(0,0,0)
z=213
w=160
color2=white
color1=blue
k=0
win=False

for j in range (0,3):
    for i in range (0,3):
        pygame.draw.rect(screen,color1,(z*i,w*j,213,160))
        color1,color2=color2,color1
pygame.display.update()

d ={1:'*' ,2:'*' ,3:'*' ,4:'*' ,5:'*' ,6:'*' ,7:'*' ,8:'*' ,9:'*'}
d1= {(0,0):1,(213,0):2,(426,0):3,(0,160):4,(213,160):5,(426,160):6,(0,320):7,(213,320):8,(426,320):9}
def checkwin():
    global win
    global color1
    global color2
    
    def  text(msg,x,y,color):
        fontobj=pygame.font.SysFont('freesans',32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
        
    for n in range(1,10,3):
        if d[n]==d[n+1]==d[n+2]!='*':
            win =True
            winner=d[n]
            
    for n in range(1,4,1):
        if d[n]==d[n+3]==d[n+6]!='*':
            win =True
            winner=d[n]

    if d[1] == d[5] == d[9] and d[1]!='*':
        win =True
        winner=d[1]
        
    if d[7] == d[5] == d[3] and d[7]!='*':
        win = True
        winner=d[7]
        
    if win==True:
        color2=white
        color1=blue
        for j in range (0,3):
            for i in range (0,3):
                 pygame.draw.rect(screen,color1,(z*i,w*j,213,160))
                 color1,color2=color2,color1
        text ('Player '+winner+' wins.',10,10,black)
        pygame.display.update()       
    if '*' not in d.values() and win ==False:
        color2=white
        color1=blue
        for j in range (0,3):
            for i in range (0,3):
                 pygame.draw.rect(screen,color1,(z*i,w*j,213,160))
                 color1,color2=color2,color1
        text ('Game Tied',10,10,black)
        pygame.display.update()               
        
    
    
    

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type== pygame.MOUSEMOTION:
            a=event.pos
        
        elif event.type== pygame.MOUSEBUTTONDOWN and event.button == 1:
            x=a[0]-a[0]%213
            y=a[1]-a[1]%160
            if d[d1[x,y]]!='o' and d[d1[x,y]]!='x':
                if k==0 and d[d1[x,y]]!='o' and d[d1[x,y]]!='x':
                    pygame.draw.line(screen,black,(x,y),(x+213,y+160),3)
                    pygame.draw.line(screen,black,(x+213,y),(x,y+160),3)
                    d[d1[(x,y)]]='x'
                    print (d)
                if k==1 and d[d1[x,y]]!='o' and d[d1[x,y]]!='x':
                    pygame.draw.ellipse(screen,black,(x,y,213,160),3)
                    d[d1[(x,y)]]='o'
                    print (d)
                k=k+1
                if k>1:
                    k=0
                checkwin()
    while win:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()      
                
    pygame.display.update()
