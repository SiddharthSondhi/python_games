# FROGGER

# imports
import pygame
from pygame.locals import *
import random
import os

# initializes pygame
pygame.init()

# colors
black = (0, 0, 0)


def show_text(msg, x, y, text_color, size):
    # draws text on screen when called.

    fontobj = pygame.font.SysFont('Times New Roman', size)
    msgobj = fontobj.render(msg, False, text_color)
    screen.blit(msgobj, (x, y))


def cars_reset():
    global car
    global lane_speeds
    lane_speeds = {}
    for lane in range(0, 6):
        lane_speeds[lane] = random.choice([1, 1.5, 2, 2.5, 3])

    for car_number in range(0, len(car) - 1):
        car[car_number] = None
    car = []
    lanecount = 0

    for loop_count in range(0, 6):
        car.append(CarsTrucks(lanecount, lane_speeds[lanecount]))
        lanecount = lanecount + 1


def create_lanes():
    # creates a dictionaries of lanes with random speeds.

    global lane_speeds
    for i in range(0, 6):
        lane_speeds[i] = random.choice([1, 1.5, 2, 2.5, 3])


def create_cars_trucks():
    lanecount = 0
    for i in range(0, 6):
        car.append(CarsTrucks(lanecount, lane_speeds[lanecount]))
        lanecount = lanecount + 1


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jumplist = []
        self.jump = 0
        self.jump_animation = 0
        self.jumpcount = 0
        self.direction = 0
        for e in range(0, 5):
            self.jumplist.append(pygame.transform.flip(pygame.image.load('jump' + str(e) + '.png'), False, True))
        self.stand = pygame.transform.flip(pygame.image.load('stand.png'), False, True)
        print('frog size', self.stand.get_rect())
        self.jumplist.append(self.stand)
        self.jumplist.append(self.stand)

    def update(self):
        if self.jump is 0:
            if self.direction is 0:
                    screen.blit(self.stand, (self.x, self.y))
            if self.direction is 1:
                    screen.blit(pygame.transform.rotate(self.stand, 90), (self.x, self.y))
            if self.direction is 2:
                    screen.blit(pygame.transform.rotate(self.stand, 180), (self.x, self.y))
            if self.direction is 3:
                    screen.blit(pygame.transform.rotate(self.stand, 270), (self.x, self.y))
        if self.jump is 1:
            if self.direction is 0:
                screen.blit(self.jumplist[self.jump_animation], (self.x, self.y))
            if self.direction is 1:
                screen.blit(pygame.transform.rotate(self.jumplist[self.jump_animation], 90), (self.x, self.y))
            if self.direction is 2:
                screen.blit(pygame.transform.rotate(self.jumplist[self.jump_animation], 180), (self.x, self.y))
            if self.direction is 3:
                screen.blit(pygame.transform.rotate(self.jumplist[self.jump_animation], 270), (self.x, self.y))
            if self.jumpcount is 3:
                self.jump_animation = self.jump_animation+1
                if self.direction is 0:
                    self.y = self.y - 11.14
                if self.direction is 1 and self.x > 28.5:
                    self.x = self.x - 11.14
                if self.direction is 2 and self.y < 564.5:
                    self.y = self.y + 11.14
                if self.direction is 3 and self.x < 790.5:
                    self.x = self.x + 11.14
                self.jumpcount = 0
            self.jumpcount = self.jumpcount + 1
            if self.jump_animation is 7:
                self.jump = 0
                self.jump_animation = 0


class BackgroundClass:
    def __init__(self, background_list):
        self.background_list = background_list
        self.list_count = 0
        self.x = 0
        self.y = 0
        self.counter = 0
        self.road = pygame.image.load('road.png')
        self.water = pygame.image.load('water.png')
        self.sidewalk = pygame.transform.scale(pygame.image.load('sidewalk.png'), (78, 78))
        self.top_road = pygame.image.load('top_road.png')
        self.bottom_road = pygame.image.load('bottom_road.png')
        self.sidewalk_list = [0.1, 0.2, 0.3, 0.4]
        for loop_count in range(0, 88):
            self.tile = self.background_list[self.list_count]
            if self.tile is 0:
                self.background_list[self.list_count] = random.choice(self.sidewalk_list)
            self.list_count = self.list_count + 1
        self.list_count = 0
        self.bg = pygame.Surface((858, 624))
        for b in range(0, 8):
            for loop_count in range(0, 11):
                self.tile = self.background_list[self.list_count]
                if self.tile is 0.1:
                    self.tile_select = pygame.transform.rotate(self.sidewalk, 90)
                if self.tile is 0.2:
                    self.tile_select = pygame.transform.rotate(self.sidewalk, 180)
                if self.tile is 0.3:
                    self.tile_select = pygame.transform.rotate(self.sidewalk, 270)
                if self.tile is 0.4:
                    self.tile_select = pygame.transform.rotate(self.sidewalk, 360)
                if self.tile is 1:
                    self.tile_select = self.road
                if self.tile is 2:
                    self.tile_select = self.bottom_road
                if self.tile is 3:
                    self.tile_select = self.top_road
                self.bg.blit(self.tile_select, (self.x, self.y))
                self.list_count = self.list_count + 1
                if self.list_count is 88:
                    self.list_count = 0
                self.x = self.x + 78
            self.x = 0
            self.y = self.y + 78
        self.x = 0
        self.y = 0

    def update(self):
        screen.blit(self.bg, (0, 0))


class CarsTrucks:
    def __init__(self, lanecount, speed):
        self.lanecount = lanecount
        self.speed = speed
        self.image_name = random.choice(['car0.png', 'car1.png', 'car2.png', 'car3.png', 'car4.png', 'truck0.png',
                                         'truck1.png'])
        self.image = pygame.image.load(self.image_name)
        if self.image_name is 'car3.png' or self.image_name is 'car4.png':
            self.image = pygame.transform.scale(self.image, (139, 69))
        if self.image_name[0:3] == 'car':
            self.x = random.randint(-140, -100)
        elif self.image_name == 'truck0.png':
            self.x = random.randint(-230, -180)
        elif self.image_name == 'truck1.png':
            self.x = random.randint(-450, -340)
        if self.lanecount == 0:
            self.y = 78 + 3
        elif self.lanecount == 1:
            self.y = 78 * 2 + 3
        elif self.lanecount == 2:
            self.y = 78 * 3 + 3
        elif self.lanecount == 3:
            self.y = 78 * 4 + 3
        elif self.lanecount == 4:
            self.y = 78 * 5 + 3
        elif self.lanecount == 5:
            self.y = 78 * 6 + 3

    def update(self):
        screen.blit(self.image, (self.x, self.y))
        self.x = self.x + self.speed


class HealthClass:
    def __init__(self):
        self.heart_full = pygame.transform.scale(pygame.image.load('heart_full.png'), (65, 65))
        self.heart_empty = pygame.transform.scale(pygame.image.load('heart_empty.png'), (65, 65))
        self.hearts = 3

    def update(self):
        if self.hearts == 3:
            screen.blit(self.heart_full, (50, 5))
            screen.blit(self.heart_full, (130, 5))
            screen.blit(self.heart_full, (210, 5))
        if self.hearts == 2:
            screen.blit(self.heart_full, (50, 5))
            screen.blit(self.heart_full, (130, 5))
            screen.blit(self.heart_empty, (210, 5))
        if self.hearts <= 1:
            screen.blit(self.heart_full, (50, 5))
            screen.blit(self.heart_empty, (130, 5))
            screen.blit(self.heart_empty, (210, 5))

    def reset_health(self):
        self.hearts = 3


class Button:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def update(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        print('button')

    def check_click(self, button_event, do_this):
        if button_event.type == pygame.MOUSEBUTTONDOWN and button_event.button == 1:
            if self.x <= button_event.pos[0] <= self.x + self.width and self.y <= button_event.pos[1] \
                    <= self.y + self.height:
                if do_this is exit:
                    pygame.quit()
                    exit()
                else:
                    do_this()


def main_loop():
    while True:

        clock.tick(60)
        pygame.display.update()
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.event.poll()
        keys = pygame.key.get_pressed()
        if keys[K_w] and frog.jump == 0:
            frog.direction = 0
            frog.jump = 1
        if keys[K_s] and frog.jump == 0:
            frog.direction = 2
            frog.jump = 1
        if keys[K_d] and frog.jump == 0:
            frog.direction = 3
            frog.jump = 1
        if keys[K_a] and frog.jump == 0:
            frog.direction = 1
            frog.jump = 1
        if keys[K_ESCAPE]:
            pygame.quit()
            exit()
        background.update()
        frog.update()
        health.update()
        for i in car:
            i.update()

            if i.x < frog.x + 25 < i.x + 139 and i.y < frog.y + 25 < i.y + 69 and i.image_name[0:3] == 'car':
                health.hearts = health.hearts - 1
                frog.jump = 0
                frog.jump_animation = 0
                frog.jumpcount = 0
                frog.x = 400.5
                frog.y = 564.5
                frog.direction = 0
            if i.x < frog.x + 25 < i.x + 176 and i.y < frog.y + 25 < i.y + 64 and i.image_name == 'truck0.png':
                health.hearts = health.hearts - 1
                frog.jump = 0
                frog.jump_animation = 0
                frog.jumpcount = 0
                frog.x = 400.5
                frog.y = 564.5
                frog.direction = 0
            if i.x < frog.x + 25 < i.x + 284 and i.y < frog.y + 25 < i.y + 64 and i.image_name == 'truck1.png':
                health.hearts = health.hearts - 1
                frog.jump = 0
                frog.jump_animation = 0
                frog.jumpcount = 0
                frog.x = 400.5
                frog.y = 564.5
                frog.direction = 0
            if 180 > i.x >= 180 - lane_speeds[i.lanecount]:
                car.append(CarsTrucks(i.lanecount, lane_speeds[i.lanecount]))

            if i.x > 858:
                car.remove(i)
        screen_resize = pygame.transform.scale(screen, window_size)
        window.blit(screen_resize, (0, 0))

        if health.hearts <= 0:
            cars_reset()
            health.reset_health()
            break

# sets window starting position to top left corner.
os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"
# Creates window on which screen which screen will be resized and blit. (No argument means full screen)
window = pygame.display.set_mode()
# Gets size of highest resolution monitor can support and is later used to resize the window.
window_size = (pygame.display.list_modes())[0]

# a dictionary in which lanes and their speeds are stored.
lane_speeds = {}
# randomly creates and inserts speeds for each lane in the lane_speeds dictionary.
create_lanes()

# list of objects of the CarsTrucks class.
car = []


create_cars_trucks()


lvl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# object creation
background = BackgroundClass(lvl)
frog = Character(400.5, 564.5)
health = HealthClass()
b1 = Button(500, 500, 100, 100, (45, 98, 65))
button_x = (window_size[0] / 858) * 500
button_y = (window_size[1] / 624) * 500

screen = pygame.Surface((858, 624))

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    pygame.display.update()
    screen.fill((170, 170, 255))
    show_text("FROGGER", 123, 123, black, 50)

    b1.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_x <= event.pos[0] <= button_x + b1.width and button_y <= event.pos[1] <= button_y + b1.height:
                main_loop()
        pygame.event.poll()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            exit()
    screen_resize = pygame.transform.scale(screen, window_size)
    window.blit(screen_resize, (0, 0))
