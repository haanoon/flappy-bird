import pygame
from pygame.locals import K_SPACE, K_UP, KEYDOWN

def is_tap_event(event):
    m_left, _, _ = pygame.mouse.get_pressed()
    space_or_up = event.type == KEYDOWN and (
        event.key == K_SPACE or event.key == K_UP
    )
    screen_tap = event.type == pygame.FINGERDOWN
    return m_left or space_or_up or screen_tap
