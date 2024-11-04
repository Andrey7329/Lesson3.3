import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/svetovoy-tir.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Начальные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Переменные для движения мишени
target_speed_x = random.choice([-1, 1])
target_speed_y = random.choice([-1, 1])

# Генерируем случайный цвет фона
background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



# Счетчик попаданий
score = 0
font = pygame.font.Font(None, 36)


running = True
while running:
    # Фон игры
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счетчик
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Меняем цвет

    # Двигаем мишень
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на столкновение с границами экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y *= -1

    # Рисуем мишень
    screen.blit(target_img, (target_x, target_y))

    # Отображаем счетчик попаданий
    score_text = font.render(f"Счет: {score}", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH - 150, 10))

    pygame.display.update()

pygame.quit()