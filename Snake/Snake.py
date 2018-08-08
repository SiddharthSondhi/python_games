# SNAKE GAME

# imports
import pygame
import random
from time import sleep
from pygame.locals import *
import os
import time

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Initializes pygame.
pygame.init()


# functions
def show_text(msg, x, y, text_color, size, font):
    fontobj = pygame.font.SysFont(font, size)
    msgobj = fontobj.render(msg, False, text_color)
    screen.blit(msgobj, (x, y))


def start_button_draw():
    start_button_image = pygame.transform.scale(pygame.image.load("start_button.png"), (500, 200))
    screen.blit(start_button_image, (700, 800))


def close_button_draw():
    close_button_image = pygame.transform.scale(pygame.image.load("close_button.png"), (100, 100))
    screen.blit(close_button_image, (1800, 10))


def level_1_button_draw():
    level_1_button_image = pygame.transform.scale(pygame.image.load("level_1_button.png"), (250, 250))
    screen.blit(level_1_button_image, (150, 100))


def level_2_button_draw():
    level_2_button_image = pygame.transform.scale(pygame.image.load("level_2_button.png"), (250, 250))
    screen.blit(level_2_button_image, (410, 100))


def menu_event_loop():
    # Same as in the other other main loop, except this also checks when the mouse is clicked on the button.

    for event in pygame.event.get():
        start_button.check_click(event, level_screen_loop)
        close_button.check_click(event, exit)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()


def level_screen_event_loop():
    for event in pygame.event.get():
        level_1_button.check_click(event, lambda: main_loop(1))
        level_2_button.check_click(event, lambda: main_loop(2))
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()


def screen_scale():
    screen_resize = pygame.transform.scale(screen, window_size)
    window.blit(screen_resize, (0, 0))


# classes
class Segment:
    """Creates a Segment that is used as a base for drawing the snake surface with changing colors. The food also uses
    this as its base."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    """This class creates a snake head on top of a segment and contains a list of coordinates. Also contains the snake
    movement. As the Snake head touches food the segments are added on the back of the snake head which follow its
    movements. As the snake goes to the edge of the screen it's coordinates are moved to the other side."""

    def __init__(self):
        self.coordinate_list = []
        self.x = (random.randint(0, 1890 // 10) * 10)
        self.y = (random.randint(0, 1170 // 10) * 10)
        self.snake_head = Segment(self.x, self.y)
        self.w, self.s, self.a, self.d = False, False, False, False
        self.coordinate_list.append((self.x, self.y))
        self.turn_position = (0, 0)
        self.turn = False
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.score = 0

    def move(self, move_event):
        if move_event.type == KEYDOWN:
            self.turn = True
            if move_event.key == K_w and self.s is not True:
                self.w = True
                self.s, self.a, self.d = False, False, False
            if move_event.key == K_s and self.w is not True:
                self.s = True
                self.w, self.a, self.d = False, False, False
            if move_event.key == K_a and self.d is not True:
                self.a = True
                self.s, self.w, self.d = False, False, False
            if move_event.key == K_d and self.a is not True:
                self.d = True
                self.s, self.a, self.w = False, False, False

    def update(self):

        if self.w is True:
            self.snake_head.y = self.snake_head.y - 10
        if self.s is True:
            self.snake_head.y = self.snake_head.y + 10
        if self.a is True:
            self.snake_head.x = self.snake_head.x - 10
        if self.d is True:
            self.snake_head.x = self.snake_head.x + 10

        if self.snake_head.x > 1910:
            self.snake_head.x = 0
        elif self.snake_head.x < 0:
            self.snake_head.x = 1910
        elif self.snake_head.y < 0:
            self.snake_head.y = 1190
        elif self.snake_head.y > 1190:
            self.snake_head.y = 0

        self.coordinate_list.pop()
        self.coordinate_list.insert(0, (self.snake_head.x, self.snake_head.y))

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for i in self.coordinate_list:
            pygame.draw.rect(screen, self.color, i + (10, 10))

        self.score = len(self.coordinate_list)

        show_text(str((self.score-1)//5), 950, 5, white, 50, 'Comic Sans MS')

    def collide_self(self):
        if (self.snake_head.x, self.snake_head.y) in self.coordinate_list[1:]:
            return True

    def add_segment(self):
        if len(self.coordinate_list) < 2:
            if self.w is True:
                self.coordinate_list.append((self.coordinate_list[-1][0], self.coordinate_list[-1][1] + 10))
            if self.s is True:
                self.coordinate_list.append((self.coordinate_list[-1][0], self.coordinate_list[-1][1] - 10))
            if self.a is True:
                self.coordinate_list.append((self.coordinate_list[-1][0] + 10, self.coordinate_list[-1][1]))
            if self.d is True:
                self.coordinate_list.append((self.coordinate_list[-1][0] - 10, self.coordinate_list[-1][1]))
        else:
            self.coordinate_list.append(self.coordinate_list[-1])


class Food:
    """Creates a food object that uses surface as it's base. As the snake touches this object, the food is moved to
     another randomly selected place on the screen."""
    def __init__(self):
        self.x = (random.randint(0, 1890 // 30) * 30)
        self.y = (random.randint(0, 1170 // 30) * 30)
        self.food_surface = pygame.Surface((30, 30))
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.rect(self.food_surface, self.color, (0, 0, 30, 30))
        screen.blit(self.food_surface, (self.x, self.y))

    def redraw(self):
        self.x = (random.randint(0, 1890 // 30) * 30)
        self.y = (random.randint(0, 1170 // 30) * 30)


class Button:
    """Creates a button that detects when clicked on."""
    def __init__(self, x, y, width, height, button_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = button_color

    def update(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def check_click(self, button_event, do_this):
        if button_event.type == pygame.MOUSEBUTTONDOWN and button_event.button == 1:
            if self.x * scale_factor_x <= button_event.pos[0] <= (self.x + self.width) * scale_factor_x and \
               self.y * scale_factor_y <= button_event.pos[1] <= (self.y + self.height) * scale_factor_y:
                if do_this is exit:
                    pygame.quit()
                    exit()
                else:
                    do_this()


class Obstacle:
    """Creates an obstacle. Snake dies when it touches it."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, surface):
        pygame.draw.rect(surface, red, (self.x, self.y, 10, 10))


def main_loop(level):
    # Main loop of the game that is called when the start game button is clicked. Has the settings for framerate. Also
    # has all the updates for classes that are called everytime it loops ,and it fills the screen black which is then
    # drawn over by the updates. Also has head collision with food.

    # Functions

    def main_event_loop(pause):
        # Function which processes the event or keypresses in the mainloop. Also passes the event to snake.move for
        # snake movement. Closes game when escape is pressed.
        for main_event in pygame.event.get():
            snake.move(main_event)
            if main_event.type == KEYDOWN:
                if main_event.key == K_ESCAPE:
                        pause = True

        while pause:
            for main_event in pygame.event.get():
                if main_event.type == KEYDOWN:
                    if main_event.key == K_SPACE or main_event.key == K_RETURN:
                        pause = False
                    if main_event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
            show_text("ESCAPE TO EXIT", 310, 200, white, 150, 'Comic Sans MS')
            show_text("SPACE TO CONTINUE", 160, 600, white, 150, 'Comic Sans MS')
            pygame.display.update()
            screen_scale()

    def collision():
        # Creates 2 variables (head_coordinates and food_coordinates) which are used to check when the sake head and
        # food collide using the colliderect function.
        head_coordinates = pygame.Rect((snake.snake_head.x, snake.snake_head.y, 10, 10))
        food_coordinates = pygame.Rect((food.x, food.y, 30, 30))

        if head_coordinates.colliderect(food_coordinates):
            food.redraw()
            food_coordinates = pygame.Rect((food.x, food.y, 30, 30))
            for i in snake.coordinate_list:
                if food_coordinates.colliderect(i + (10, 10)):
                    food.redraw()
            snake.add_segment()
            snake.add_segment()
            snake.add_segment()
            snake.add_segment()
            snake.add_segment()

    def obstacle_collision():
        head_coordinates = pygame.Rect((snake.snake_head.x, snake.snake_head.y, 10, 10))
        for i in obstacles:
            if head_coordinates.colliderect(i.get_rect()):
                return True

    def game_over():
        show_text("Game Over", 420, 5, white, 200, 'Comic Sans MS')
        screen_scale()
        pygame.display.update()
        time.sleep(2)
        pygame.mouse.set_visible(True)

    def level_create(level):
        global obstacles
        obstacles = {}
        if level == 2:
            surface_1 = pygame.Surface((1920, 10))
            surface_2 = pygame.Surface((1920, 10))
            surface_3 = pygame.Surface((10, 1200))
            surface_4 = pygame.Surface((10, 1200))
            for i in range (0, 1920, 10):
                obstacle = Obstacle(i, 0)
                obstacle.update(surface_1)
            for i in range (0, 1920, 10):
                obstacle = Obstacle(i, 0)
                obstacle.update(surface_2)
            for i in range (0, 1200, 10):
                obstacle = Obstacle(0, i)
                obstacle.update(surface_3)
            for i in range (0, 1200, 10):
                obstacle = Obstacle(0, i)
                obstacle.update(surface_4)
            obstacles[surface_1] = (0, 0)
            obstacles[surface_2] = (0, 1190)
            obstacles[surface_3] = (0,0)
            obstacles[surface_4] = (1910, 0)

    def level_draw(level):
        for i in obstacles:
            screen.blit(i, obstacles[i])

    # object declaration
    food = Food()
    snake = Snake()
    is_paused = False

    pygame.mouse.set_visible(False)

    level_create(level)

    # Main loop itself
    while True:

        # framerate setting
        clock.tick(60)

        # This line updates the changes that have occurred before onto the screen.
        pygame.display.update()

        # Fills the screen black so that objects can be drawn over it again.(note that the screen isn't filled black
        # until the pygame.update)
        screen.fill(black)

        # Update method in snake is called
        snake.update()

        # calls the food update method
        food.update()

        level_draw(level)

        # Main event loop is called
        main_event_loop(is_paused)

        # Collision function is called
        collision()

        if snake.collide_self():
            game_over()
            return
        if obstacle_collision():
            game_over()
            return

        # resizes the screen so it's fullscreen
        screen_scale()

level_1_button = Button(150, 100, 250, 250, black)
level_2_button = Button(410, 100, 250, 250, black)


def level_screen_loop():

    while True:
        # sets the framerate.
        clock.tick(60)

        # updates the display to show what changes have happened.
        pygame.display.update()

        # fills the screen white.
        screen.fill(black)

        level_1_button.update()
        level_1_button_draw()

        level_2_button.update()
        level_2_button_draw()

        # Calls the menu event loop function
        level_screen_event_loop()

        screen_scale()

# Also resizes the screen so it's fullscreen.
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
window_size = (pygame.display.list_modes())[0]
window = pygame.display.set_mode(window_size, pygame.FULLSCREEN | pygame.NOFRAME)
screen = pygame.Surface((1920, 1200))
scale_factor_x = window_size[0]/1920
scale_factor_y = window_size[1]/1200

# creates a call variable which can be used to set the framerate.
clock = pygame.time.Clock()

# Creates an a button object used to start the game and another to close the game.
start_button = Button(700, 800, 500, 200, white)
close_button = Button(1800, 10, 100, 100, white)


# The other main loop of the game. This runs when the game is first started. It is the menu. When the start button is
# clicked, the the other main loop or the actual game starts.
while True:
    # sets the framerate.
    clock.tick(60)

    # updates the display to show what changes have happened.
    pygame.display.update()

    # fills the screen white.
    screen.fill(white)

    # Draws text on screen
    show_text("Snake Game", 400, 5, black, 200, 'Comic Sans MS')

    # Calls the update method from the button class and calls function to draw buttons on screen.
    start_button.update()
    close_button.update()
    start_button_draw()
    close_button_draw()

    # Calls the menu event loop function
    menu_event_loop()

    screen_scale()
