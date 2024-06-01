import pygame
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=pos)

        # Параметры движения
        self.speed = 0.5  # Скорость
        self.vel_x = 0  # Скорость по оси X
        self.vel_y = 0  # Скорость по оси Y

    def update(self):
        self.vel_x = 0  # Сброс скорости по оси X
        self.vel_y = 0  # Сброс скорости по оси Y

        # Обработка нажатых клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.vel_x += self.speed
        if keys[pygame.K_UP]:
            self.vel_y -= self.speed
        if keys[pygame.K_DOWN]:
            self.vel_y += self.speed

        # Ограничение скорости
        self.vel_x = max(-self.speed, self.vel_x)
        self.vel_x = min(self.speed, self.vel_x)
        self.vel_y = max(-self.speed, self.vel_y)
        self.vel_y = min(self.speed, self.vel_y)

        # Обновление позиции
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player = Player((0, 0))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)


pygame.quit()

