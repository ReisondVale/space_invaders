import pygame

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
coordinate_x = 370
coordinate_y = 480
coordinate_x_change = 0


def player(x, y):
    screen.blit(player_image, (x, y))

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
                coordinate_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                coordinate_x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                coordinate_x_change = 0

    coordinate_x += coordinate_x_change

    if coordinate_x <= 0:
        coordinate_x = 0
    elif coordinate_x >= 736:
        coordinate_x = 736

    player(coordinate_x, coordinate_y)
    pygame.display.update()