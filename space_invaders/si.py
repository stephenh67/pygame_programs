import pygame
import math


# initialize the pygame
pygame.init()

# create the screen
screen_width = 800
screen_height = 600
player_width = 64
enemy_width = 64

screen = pygame.display.set_mode((screen_width, screen_height))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/alien.png')
pygame.display.set_icon(icon)
background = pygame.image.load('images/background.png')

# player
player_img = pygame.image.load('images/rocket.png')
player_x = (screen_width - (player_width / 2)) / 2
player_y = 525
player_x_change = 0

# alien
alien_img = pygame.image.load('images/alien.png')
enemy_x = 370
enemy_y = 80
enemy_x_change = .5
enemy_y_change = 40

# bullet
bullet_img = pygame.image.load('images/bullet.png')
bullet_x = 0
bullet_y = 480
bullet_y_change = 5
bullet_state = 'ready'

score = 0


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img, (x + 20, y + 10))


def player(x, y):
    screen.blit(player_img, (int(x), int(y)))


def enemy(x, y):
    screen.blit(alien_img, (int(x), int(y)))


def is_collision(e_x, e_y, b_x, b_y):
    distance = math.sqrt(math.pow(e_x - b_x, 2) + math.pow(e_y - b_y, 2))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:

    screen.fill((0, 0, 0))
    # set background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change -= 2.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 2.5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    # get the current x of ship
                    bullet_x = player_x
                    fire_bullet(player_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # checking for boundaries shi[
    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= screen_width - player_width:
        player_x = screen_width - player_width

    #
    enemy_x += enemy_x_change

    if enemy_x <= 0:
        enemy_x_change = .5
        enemy_y += enemy_y_change
    elif enemy_x >= screen_width - enemy_width:
        enemy_x_change = -.5
        enemy_y += enemy_y_change

    # check if bullet off screen
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = 'ready'

    # bullet movement
    if bullet_state == 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # collision
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = 'ready'
        score += 1
        print(score)
        enemy_x = 370
        enemy_y = 80

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()
