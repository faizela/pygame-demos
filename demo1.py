import pygame
from sys import exit
pygame.init()

screen_WIDTH = 800
screen_HEIGHT = 400


screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
screen.fill('Black')
pygame.display.set_caption("demo")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('Demo game', False, 'Black')
snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600

game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 60))
    snail_x_pos -= 4

    if snail_x_pos < 0:
        snail_x_pos = 800


    screen.blit(snail_surface, (snail_x_pos, 250))


    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)



