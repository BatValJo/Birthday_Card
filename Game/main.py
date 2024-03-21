import pygame
from sys import exit
from utilities import *


pygame.init()

# Game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Happy Birthday!")

# Objects
clock = pygame.time.Clock()

move_cloud = 0
scroll_city = 0

# Sky
background_images = []
for i in range(1, 5):
    background_image = pygame.image.load(f'Assets/Clouds/cloud_{i}.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, (background_image.get_width(), 400))
    background_images.append(background_image)
background_width = background_images[0].get_width()

city_surf = pygame.image.load('Assets/Happy/city.png').convert_alpha()
city_surf = pygame.transform.scale(city_surf, (500, 100))
city_width = city_surf.get_width()

running = True
while running:

    # draw world
    draw_background(background_images, window, background_width, move_cloud)
    move_cloud += 1

    draw_city(window, city_surf, city_width, scroll_city)

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
