import pygame
from sys import exit
pygame.init()

screen_WIDTH = 800
screen_HEIGHT = 400


screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
screen.fill('White')
pygame.display.set_caption("demo")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('Blue')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (200, 100))
    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)

