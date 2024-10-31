import pygame
import random

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space_ship_logo.png')
pygame.display.set_icon(icon)

# Player
player_image = pygame.image.load('space_ship_player.png')
player_coordinate_x = 370
player_coordinate_y = 480
player_coordinate_x_change = 0

# Enemy
enemy_image = pygame.image.load('enemy.png')
enemy_coordinate_x = random.randint(0, 800)
enemy_coordinate_y = random.randint(50, 150)
enemy_coordinate_x_change = 0.3
enemy_coordinate_y_change = 40


def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y):
    screen.blit(enemy_image, (x, y))

# Game loop
running = True
while running:
    # background screen
    screen.fill((192, 192, 192))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # control space ship with arrows
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_coordinate_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_coordinate_x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_coordinate_x_change = 0

    player_coordinate_x += player_coordinate_x_change

    if player_coordinate_x <= 0:
        player_coordinate_x = 0
    elif player_coordinate_x >= 736:
        player_coordinate_x = 736

    enemy_coordinate_x += enemy_coordinate_x_change

    if enemy_coordinate_x <= 0:
        enemy_coordinate_x_change = 0.3
        enemy_coordinate_y += enemy_coordinate_y_change
    elif enemy_coordinate_x >= 736:
        enemy_coordinate_x_change = -0.3
        enemy_coordinate_y += enemy_coordinate_y_change

    player(player_coordinate_x, player_coordinate_y)
    enemy(enemy_coordinate_x, enemy_coordinate_y)
    pygame.display.update()