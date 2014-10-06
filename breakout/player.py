

import sprite
import pygame


# instance of current player paddle


class Paddle(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)

        """
        Create new paddle instance
        """

        self.x = 10
        self.y = 440
        self.width = 100
        self.height = 5
        self.drag = 5
        self.timer = 0
        self.flicker = 0

    def shrink(self):

        """
        run timer for shrink
        """

        self.timer = 100
        self.width = 40
        self.x += 30

    def update(self, screen):
        sprite.Sprite.update(self, screen)

        # handle shrink prank
        if self.timer > 0:
            self.timer -= 1
            if self.timer == 1:
                self.width = 100
                self.x -= 30

        # draw sprite
        if self.flicker == 0:
            self.__draw(screen)
        else:
            self.flicker -= 1

    def __draw(self, screen):

        """
        Draw paddle on screen
        """

        pygame.draw.aalines(screen, (200, 255, 200), True,
                            [(self.x, self.y), (self.x + self.width, self.y),
                             (self.x + self.width, self.y + self.height),
                             (self.x, self.y + self.height)])


__author__ = 'dj'
