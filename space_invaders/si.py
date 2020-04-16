import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/alien.png')
pygame.display.set_icon(icon)


def player():
    screen.blit(player_img, (player_x, player_y))

# player
player_img = pygame.image.load('images/rocket.png')
player_x = 370
player_y = 400

# game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    player()
    pygame.display.update()

