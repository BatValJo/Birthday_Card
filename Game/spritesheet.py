import pygame


class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, colour):
        image = pygame.Surface((int(width), int(height))).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))  # (frame * width) -
        image.set_colorkey(colour)  # set transparency colour!
        return image
