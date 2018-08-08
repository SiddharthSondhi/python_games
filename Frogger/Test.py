import pygame
from pygame.locals import *
import random
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
import sys
from threading import Thread
#car_thread=Thread(target=functionname,args=(arguments,))
#car_thread.start()

#window=pygame.display.set_mode((858,624),RESIZABLE|HWSURFACE|DOUBLEBUF)
window=pygame.display.set_mode()
window_size=(pygame.display.list_modes())[0]
print(window_size)


def colision_detect():
        #self.image.unlock()

        for i in car:
                print('cars')
                
                i.update()

                #collision
                if i.x < frog.x+25 < i.x+139 and i.y < frog.y+25 <i.y+69 and i.image_name[0:3]== 'car':

                        frog.jump=0
                        frog.jump_animation=0
                        frog.jumpcount=0
                        frog.x=400.5
                        frog.y=564.5
                        frog.direction=0
                if i.x < frog.x+25 < i.x+176 and i.y < frog.y+25 <i.y+64 and i.image_name== 'truck0.png':
                     
                        frog.jump=0
                        frog.jump_animation=0
                        frog.jumpcount=0
                        frog.x=400.5
                        frog.y=564.5
                        frog.direction=0
                if i.x < frog.x+25 < i.x+284 and i.y < frog.y+25 <i.y+64 and i.image_name== 'truck1.png':
                   
                        frog.jump=0
                        frog.jump_animation=0
                        frog.jumpcount=0
                        frog.x=400.5
                        frog.y=564.5
                        frog.direction=0



                #Car Placement       
                if 180> i.x >=180-lane_speeds[i.lanecount] :
                        car.append(cars_trucks(i.lanecount,lane_speeds))
                
                if i.x>858:
                        car.remove(i)
        window.fill((0,0,0))

class background_class:
	def __init__(self,background_list):
		self.background_list=background_list
		self.list_count=0
		self.x=0
		self.y=0
		self.counter=0
		self.road=pygame.image.load('road.png')
		self.water=pygame.image.load('water.png')
		self.sidewalk=pygame.transform.scale(pygame.image.load('sidewalk.png'),(78,78))
		self.top_road=pygame.image.load('top_road.png')
		self.bottom_road=pygame.image.load('bottom_road.png')
		self.sidewalk_list=[0.1,0.2,0.3,0.4]
		for i in range (0,88):
			self.tile=self.background_list[self.list_count]
			if self.tile==0:
				self.background_list[self.list_count]=random.choice(self.sidewalk_list)
			self.list_count=self.list_count+1
		self.list_count=0
		self.bg=pygame.Surface((858,624))
		for b in range(0,8):
			for i in range(0,11):
				self.tile=self.background_list[self.list_count]
				if self.tile==0.1:
					self.tile_select=pygame.transform.rotate(self.sidewalk,90)
				if self.tile==0.2:
					self.tile_select=pygame.transform.rotate(self.sidewalk,180)
				if self.tile==0.3:
					self.tile_select=pygame.transform.rotate(self.sidewalk,270)
				if self.tile==0.4:
				       self.tile_select=pygame.transform.rotate(self.sidewalk,360)
				if self.tile==1:
					self.tile_select=self.road
				if self.tile==2:
					self.tile_select=self.bottom_road
				if self.tile==3:
					self.tile_select=self.top_road
				self.bg.blit(self.tile_select,(self.x,self.y))
				self.list_count=self.list_count+1
				if self.list_count ==88:
					self.list_count=0
				self.x=self.x+78
			self.x=0
			self.y=self.y+78
		self.x=0
		self.y=0

		
	#background blit
	
	def update(self):
		#screen.fill((0,0,0))
		screen.blit(self.bg,(0,0))

class character:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.jumplist=[]
		self.jump=0
		self.jump_animation=0
		self.jumpcount=0
		self.direction=0
		for e in range (0,5):
			self.jumplist.append(pygame.transform.flip(pygame.image.load('jump'+str(e)+'.png'),False,True)) 
		self.stand=pygame.transform.flip(pygame.image.load('stand.png'),False,True)
		print('frog size',self.stand.get_rect())
		self.jumplist.append(self.stand)
		self.jumplist.append(self.stand)

		
	#Frog Movement
		
	def update(self):
		if self.jump==0:
			if self.direction==0:
				screen.blit(self.stand,(self.x,self.y))
			if self.direction==1:
				screen.blit(pygame.transform.rotate(self.stand,90),(self.x,self.y))
			if self.direction==2:
				screen.blit(pygame.transform.rotate(self.stand,180),(self.x,self.y))
			if self.direction==3:
				screen.blit(pygame.transform.rotate(self.stand,270),(self.x,self.y))
		if self.jump==1:
			if self.direction==0:
				screen.blit(self.jumplist[self.jump_animation],(self.x,self.y))
			if self.direction==1:
				screen.blit(pygame.transform.rotate(self.jumplist[self.jump_animation],90),(self.x,self.y))
			if self.direction==2:
				screen.blit(pygame.transform.rotate(self.jumplist[self.jump_animation],180),(self.x,self.y))
			if self.direction==3:
				screen.blit(pygame.transform.rotate(self.jumplist[self.jump_animation],270),(self.x,self.y))
			if self.jumpcount==3:
				self.jump_animation=self.jump_animation+1
				if self.direction==0:
					self.y=self.y-11.14
				if self.direction==1 and self.x > 28.5:
					self.x=self.x-11.14
				if self.direction==2 and self.y < 564.5:
					self.y=self.y+11.14
				if self.direction==3 and self.x < 790.5:
					self.x=self.x+11.14
				self.jumpcount=0
			self.jumpcount=self.jumpcount+1
			if self.jump_animation==7:
				self.jump=0
				self.jump_animation=0




class cars_trucks:
        def __init__(self,lanecount,lane_speeds):
                self.lanecount=lanecount
                self.speed=lane_speeds[lanecount]
                self.image_name=random.choice(['car0.png','car1.png','car2.png','car3.png','car4.png','truck0.png','truck1.png'])
                self.image= pygame.image.load(self.image_name)
                if self.image_name==('car3.png') or self.image_name==('car4.png'):
                        print('asjdhfiu')
                        self.image=pygame.transform.scale(self.image,(139,69))
                if self.image_name[0:3]=='car':
                        #print('carsize',self.image.get_rect())
                        self.x=random.randint(-140,-100)
                elif  self.image_name=='truck0.png':
                        self.x=random.randint(-230,-180)
                        #print('truck0size',self.image.get_rect())
                elif  self.image_name=='truck1.png':
                        self.x=random.randint(-450,-340)
                        #print('truck1size',self.image.get_rect())
                if self.lanecount==0:
                        self.y=78+3
                elif self.lanecount==1:
                        self.y=78*2+3
                elif self.lanecount==2:
                        self.y=78*3+3        
                elif self.lanecount==3:
                        self.y=78*4+3
                elif self.lanecount==4:
                        self.y=78*5+3
                elif self.lanecount==5:
                        self.y=78*6+3
                

        def update(self):
                screen.unlock()
                screen.blit(self.image,(self.x,self.y))
                self.x=self.x+self.speed

global lane_speeds
lane_speeds={}
for i in range(0,6):
        lane_speeds[i]=random.choice([1,1.5,2,2.5,3])


global car
car=[]                  


lanecount=0

for i in range(0,6):
        car.append(cars_trucks(lanecount,lane_speeds))
        lanecount=lanecount+1






lvl=   [0,0,0,0,0,0,0,0,0,0,0,
	3,3,3,3,3,3,3,3,3,3,3,
	1,1,1,1,1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,1,1,1,1,
	1,1,1,1,1,1,1,1,1,1,1,
	2,2,2,2,2,2,2,2,2,2,2,
	0,0,0,0,0,0,0,0,0,0,0]

frog=character(400.5,564.5)


background=background_class(lvl)
screen=pygame.Surface((858,624))



car_thread=Thread(target=colision_detect)

car_enable=0

while True:
        pygame.display.update()
        for event in pygame.event.get():
                if event.type==QUIT :
                        pygame.quit()
                        sys.exit()
                
        pygame.event.poll()
        keys = pygame.key.get_pressed()
        if keys[K_w] and frog.jump==0:
                frog.direction=0
                frog.jump=1
        if keys[K_s] and frog.jump==0:
                frog.direction=2
                frog.jump=1
        if keys[K_d] and frog.jump==0:
                frog.direction=3
                frog.jump=1
        if keys[K_a] and frog.jump==0:
                frog.direction=1
                frog.jump=1
        if keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
        if car_enable==0:
                car_thread.start()
                car_enable=1
                 
        
        #screen.fill((0,0,0))
        background.update()
        frog.update()
        
         

        screen_resize=pygame.transform.scale(screen,window_size)
        window.blit(screen_resize,(0,0))
        
