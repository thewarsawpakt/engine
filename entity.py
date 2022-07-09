import pygame
import os


class Entity(pygame.sprite.Sprite):
    def __init__(self, position: list[int, int], image: str | pygame.Surface):
        if os.path.exists(image):
            self.image = pygame.image.load(image)
        else:
            self.image = image

        self.rect = self.image.get_rect()
        self.rect.move_ip(*position)