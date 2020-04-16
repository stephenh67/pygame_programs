import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/alien.png')
pygame.display.set_icon(icon)


def player(x, y):
    screen.blit(player_img, (x, y))


# player
player_img = pygame.image.load('images/rocket.png')
player_x = 370
player_y = 400
player_x_change = 5

# game loop
running = True
while running:

    screen.fill((0, 0, 0))
    player_x += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow")
            if event.key == pygame.K_RIGHT:
                print('Right arrow')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("key released")
    player(player_x, player_y)
    pygame.display.update()

