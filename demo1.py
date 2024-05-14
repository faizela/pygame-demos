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

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Demo game', False, 'Black').convert()


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(800, 300))
print(snail_rect.left)

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 60))
    snail_rect.left -= 4

    if snail_rect.left < 0:
        snail_rect.left = 800

    player_rect.left += 1

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print('collision')

    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)



