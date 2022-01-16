from sys import exit
from time import sleep
from random import randint

import pygame

X = 850
Y = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
YELLOW = (255, 255, 0)
BROWN = (150, 75, 0)
selected_color = BLUE
positions = []
last_positions = []

sc = pygame.display.set_mode((X, Y))

panel = pygame.Surface((250, Y))
canvas = pygame.Surface((X-250, Y))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()


class SelectColor:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.item = pygame.Surface((self.width, self.height))

    def update(self):
        global selected_color
        global panel

        position_x, position_y = pygame.mouse.get_pos()
        pressed_item = pygame.mouse.get_pressed()
        if pressed_item[0] and position_x > self.x and position_x < self.width+self.x and position_y > self.y and position_y < self.height+self.y:
            selected_color = self.color

        panel.blit(self.item, (self.x, self.y))

        self.item.fill(self.color)


select_white = SelectColor(50, 50, 50, 50, WHITE)
select_red = SelectColor(150, 50, 50, 50, RED)
select_green = SelectColor(50, 150, 50, 50, GREEN)
select_blue = SelectColor(150, 150, 50, 50, BLUE)
select_orange = SelectColor(50, 250, 50, 50, ORANGE)
select_pink = SelectColor(150, 250, 50, 50, PINK)
select_yellow = SelectColor(50, 350, 50, 50, YELLOW)
select_brown = SelectColor(150, 350, 50, 50, BROWN)


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    clock.tick(60)

    pressed = pygame.mouse.get_pressed()
    position = pygame.mouse.get_pos()
    if pressed[0] and position[0] >= 250:
        positions.append(position)
        last_positions.append(position)
        for i in range(len(positions)):
            x_pos_line = positions[i][0]
            y_pos_line = positions[i][1]
            last_x_pos_line = positions[i-1][0]
            last_y_pos_line = positions[i-1][1]
            if i > 1:
                pygame.draw.aaline(canvas, selected_color, [last_x_pos_line-250, last_y_pos_line], [x_pos_line-250, y_pos_line], 10)
            else:
                pygame.draw.aaline(canvas, selected_color, [x_pos_line-250, y_pos_line], [x_pos_line-250, y_pos_line], 10)
    else:
        positions = []

    keys = pygame.key.get_pressed()

    if keys[pygame.K_c]:
        canvas.fill(BLACK)
        positions = []
        last_positions = []
    elif keys[pygame.K_s]:
        pygame.image.save(canvas, f"screen{randint(1, 1000000)}.png")
        sleep(1)

    panel.fill(GRAY)

    select_white.update()
    select_red.update()
    select_green.update()
    select_blue.update()
    select_orange.update()
    select_pink.update()
    select_yellow.update()
    select_brown.update()

    sc.blit(canvas, (250, 0))
    sc.blit(panel, (0, 0))

    pygame.display.update()