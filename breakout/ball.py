
#
#   ball sprite for paddle
#

import random
import sprite
import pygame


class Ball(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)

        """
        init new ball
        """

        self.width = 8
        self.height = 8
        self.score = 0

    def throw(self):

        """
        throw ball at random angle
        """

        self.vx = (2 * random.random()) - 1
        self.vy = (4 * random.random()) + 4

    def update(self, screen, player=None):
        sprite.Sprite.update(self, screen)

        """
        check collision with player, and update ball position
        """

        # prevent ball from leaving screen
        if self.x < 0 or self.x > 632:
            self.vx = -self.vx
        if self.y < 0:
            self.vy = -self.vy
            if self.vx == 0:
                self.throw()

        # if we have bounce with paddle, reverse direction and speed
        if self.overlap(player.left_paddle):
            self.vy = -(random.random() * 5)
            self.vy -= 5
            self.vx = -(random.random() * 15)
            self.vx -= 1
            player.sound_bounce.play()
        if self.overlap(player.right_paddle):
            self.vy = -(random.random() * 5)
            self.vy -= 5
            self.vx = (random.random() * 15)
            self.vx += 1
            player.sound_bounce.play()

        # and draw
        self.__draw(screen)

        # set score to zero
        if self.score > 0:
            self.score = 0

    def __draw(self, screen):

        """
        Draw ball on screen
        """

        pygame.draw.rect(screen, (200, 255, 200), (self.x, self.y, self.width, self.height))


__author__ = 'dj'
