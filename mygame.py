# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from random import randint as rd
from player import Player
from enemy import Enemy



# РАЗМЕРЫ ОКОШКА
WIDTH = 1000
HEIGHT = 1350
WIDTH = 1300
HEIGHT = 750

FPS = 60
FPS = 1000

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

player = Player("./capibara.png", 300, 120, 200, 200)
enemy = Enemy("./zombie.png", 100, 150, 250, 250)


enemyGroup = pygame.sprite.Group()

def spawnEnemy():
    enemy = Enemy("./zombie.png", width=rd(20, 50), height=rd(20, 50), x=rd(0, WIDTH), y=rd(0, 200))
    enemyGroup.add(enemy)

for i in range(5):
    spawnEnemy()


y = 0
x = 0

bullets = []
countHit = 0
# Цикл игры
running = True
while running:
    screen.fill(WHITE)

    for bullet in bullets:
        bullet.draw(screen)
        bullet.move()

        collideSprite = pygame.sprite.spritecollideany(bullet, enemyGroup)
        if collideSprite:
            bullets.remove(bullet)
            enemyGroup.remove(collideSprite)
            countHit += 1

    enemy.draw(screen)
    enemy.follow(player, 1)

    pygame.draw.rect(screen, GREEN, (x, 200, 50, 20))
    player.draw(screen)
    player.movement()
    if x >= WIDTH + 20:
        x = -70
    player.showHp(screen,100,100)
    for enemy in enemyGroup:
        enemy.draw(screen)
        enemy.follow(player,1)

    if pygame.sprite.spritecollideany(player, enemyGroup):
        player.hp -= 0.1
        if player.hp <= 0:
            print('ЛОООООООООООООООООООООООООООООООООООООООООХ')
            running = False


    clock.tick(FPS)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.display.update()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif  event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet = player.shoot(mouse_x, mouse_y)
                if bullet:
                    bullets.append(bullet)
pygame.quit()

# домашка 21.12.2024