# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from random import randint as rd
from player import Player

# РАЗМЕРЫ ОКОШКА
WIDTH = 500
HEIGHT = 300

FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

player = Player("./capibara.png", 100, 120, 200, 200)

y = 0
x = 0
# Цикл игры
running = True
while running:

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (x, 200, 50, 20))
    player.draw(screen)
    if x >= WIDTH + 20:
        x = -70
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x = x + 1
    elif keys[pygame.K_a]:
        x = x - 1
    if keys[pygame.K_w]:
        y = y - 1
    elif keys[pygame.K_s]:
        y = y + 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x = x + 1
    elif keys[pygame.K_a]:
        x = x - 1
    if keys[pygame.K_w]:
        y = y - 1
    elif keys[pygame.K_s]:
        y = y + 1
    pygame.display.update()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

# домашка 21.12.2024
# TODO Сделать движение вверх-вниз через клавиши, сделать проверки на пересечение верхней границы, нижней, и левой границ