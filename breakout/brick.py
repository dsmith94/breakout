

import sprite
import pygame

# class of individual brick


class Brick(sprite.Sprite):

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)

        """
        Create new instance of brick at x, y
        """

        self.width = 40
        self.height = 10
        self.x = x
        self.y = y
        self.score = 10

    def update(self, screen):
        sprite.Sprite.update(self, screen)

        # draw sprite
        self.__draw(screen)

    def __draw(self, screen):

        """
        draw brick on screen
        """

        pygame.draw.rect(screen, (200, 255, 200), (self.x, self.y, self.width, self.height))


__author__ = 'dj'
