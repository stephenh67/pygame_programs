import pygame
import take_bet as tb

from cards import Hand, Deck
from settings import Settings

pygame.init()


def play():
    """
    play button screen
    :return:
    """
    bj_settings = Settings()
    pygame.display.set_caption("Blackjack")

    # create play button rect
    play_button = pygame.image.load('images/play.png')
    play_rect = play_button.get_rect()
    play_rect.topleft = (475, 100)

    # TODO FIX
    pygame.display.set_icon(pygame.image.load('images/poker.png'))

    bj_settings.screen.fill(bj_settings.bg_color)
    bj_settings.screen.blit(play_button, (475, 50))

    pygame.display.update()

    while True:
        # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    player = Hand()
                    dealer = Hand()
                    deck = Deck()
                    tb.take_bet(1000, player, dealer, deck)



if __name__ == '__main__':
    play()