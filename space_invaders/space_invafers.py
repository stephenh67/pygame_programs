import pygame
import math
import random
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen
screen_width = 800
screen_height = 600
player_width = 64
enemy_width = 64

screen = pygame.display.set_mode((screen_width, screen_height))

mixer.music.load('sounds/background.wav')
mixer.music.play(-1)

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

# enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('images/alien.png'))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(.5)
    enemy_y_change.append(40)

# bullet
bullet_img = pygame.image.load('images/bullet.png')
bullet_x = 0
bullet_y = 480
bullet_y_change = 5
bullet_state = 'ready'


# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (text_x, text_y))

score_value = 0


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img, (int(x + 20), int(y + 10)))


def player(x, y):
    screen.blit(player_img, (int(x), int(y)))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (int(x), int(y)))


def is_collision(e_x, e_y, b_x, b_y):
    distance = math.sqrt(math.pow(e_x - b_x, 2) + math.pow(e_y - b_y, 2))
    if distance < 24:
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
                    bullet_sound = mixer.Sound('sounds/laser.wav')
                    bullet_sound.play()
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

    # enemy movement
    for i in range(num_of_enemies):
        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] <= 0:
            enemy_x_change[i] = .5
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= screen_width - enemy_width:
            enemy_x_change[i] = -.5
            enemy_y[i] += enemy_y_change[i]

        # collision
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            explosion_sound = mixer.Sound('sounds/explosion.wav')
            explosion_sound.play()
            bullet_y = 480
            bullet_state = 'ready'
            score_value += 1
            print(score_value)
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # check if bullet off screen
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = 'ready'

    # bullet movement
    if bullet_state == 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change



    player(player_x, player_y)
    show_score(text_y, text_y)

    pygame.display.update()
