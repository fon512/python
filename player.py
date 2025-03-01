import pygame


class Player:
    hp = 100
    width = 50
    height = 50
    x = 100
    y = 100
    image = ""

    speed = 2
    surface = ""
    rect = ""

    def __init__(self, image, width=50, height=50, x=100, y=100):
        self.image = image
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.surface = pygame.image.load(image)
        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))
        self.rect = self.surface.get_rect(center=(x, y))

    def draw(self, screen: pygame.Surface):
        width = screen.get_width()
        height = screen.get_height()

        if self.x < -50:
            self.x = width + 50
        elif self.x > width + 50:
            self.x = - 50
        if self.y < -50:
            self.y = height + 50
        elif self.y > height + 50:
            self.y = - 50
        self.rect.center = (self.x, self.y)
        screen.blit(self.surface, self.rect)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += self.speed
        elif keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        elif keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_LSHIFT]:
            self.speed = 4
        else:
            self.speed = 2
            #  if keys[pygame.K_j]:
    #     keys.y += 1
    #  elif keys[pygame.K_u]:
    #     keys.y -= 1
    #  if keys[pygame.K_k]:
    #     keys.x += 1
    #  elif keys[pygame.K_h]:
    #     keys.x -= 1
    def showHp(self, screen, x,y):
        pygame.draw.rect(screen, (0,0,0),(20,20, 100, 50))
        pygame.draw.rect(screen, (0,200,100), (20,20,self.hp,50))
