import pygame

from settings import Settings

pygame.init()


def play():
    """
    main game loop
    :return:
    """
    bj_settings = Settings()
    pygame.display.set_caption("Blackjack")

    # TODO FIX
    pygame.display.set_icon(pygame.image.load('images/poker.png'))

    bj_settings.screen.fill(bj_settings.bg_color)
    bj_settings.game_screen.blit(play_button, (475, 50))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



if __name__ == '__main__':
    play()