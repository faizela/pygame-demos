import pygame
from sys import exit
pygame.init()

screen_WIDTH = 800
screen_HEIGHT = 400


screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
screen.fill('Black')
pygame.display.set_caption("demo")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)

