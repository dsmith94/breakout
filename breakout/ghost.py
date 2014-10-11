
#
# ghost bricks - after a brick is dead, show a gray brick
#

import pygame
import brick


class Ghost(brick.Brick):
    def __init__(self, x, y):
        brick.Brick.__init__(self, x, y)

        """
        create ghost brick onscreen
        """

        self.timer = 10

    def update(self, screen):
        brick.Brick.update(self, screen)

        """
        update sprite
        """

        self.timer -= 1
        self.__draw(screen)

    def __draw(self, screen):

        """
        draw ghost onscreen
        """

        color = 100 + (self.timer * 10)
        pygame.draw.rect(screen, (color, color + 50, color), (self.x, self.y, self.width, self.height))

__author__ = 'dj'
