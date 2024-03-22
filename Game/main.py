import pygame
from sys import exit
from utilities import *
import spritesheet
pygame.init()
clock = pygame.time.Clock()

# Game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Happy Birthday! 💕")


# Sprite sheet
sprite_sheet_run = pygame.image.load('Assets/Daniel/Run.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_run)

BLACK = (0, 0, 0)


frame_0 = sprite_sheet.get_image(0,  183.25, 137, BLACK)
frame_1 = sprite_sheet.get_image(1,  183.25, 137, BLACK)
frame_2 = sprite_sheet.get_image(2,  183.25, 137, BLACK)

# Sky
background_images = []
for i in range(1, 5):
    background_image = pygame.image.load(f'Assets/Clouds/cloud_{i}.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, (background_image.get_width(), 400))
    background_images.append(background_image)
background_width = background_images[0].get_width()

# City
city_surf = pygame.image.load('Assets/City/city.png').convert_alpha()
city_surf = pygame.transform.scale(city_surf, (500, 100))
city_width = city_surf.get_width()

move_cloud = 0
scroll_city = 0

running = True
while running:

    # draw world
    draw_background(background_images, window, background_width, move_cloud)
    move_cloud += 1

    draw_city(window, city_surf, city_width, scroll_city)

    # Frame image
    window.blit(frame_0, (0, 0))
    window.blit(frame_1, (0, 0))
    window.blit(frame_2, (0, 0))

    # get_pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll_city > 0:
        scroll_city -= 2
    if key[pygame.K_RIGHT] and scroll_city < 1000:
        scroll_city += 2

    # draw road
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
pygame.quit()
