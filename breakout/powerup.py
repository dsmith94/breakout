
#
#   powerup sprite class
#


import pygame
import random
import sprite


class Powerup(sprite.Sprite):

    def __init__(self, level):
        sprite.Sprite.__init__(self)

        """
        create new powerup
        """

        self.width = 10
        self.height = 15
        self.y = -self.width
        self.x = int((random.random() * 630))
        self.vy = 5
        self.flicker_timer = 10
        self.level = level
        sound_spawn = pygame.mixer.Sound('./breakout/spawn.ogg')
        sound_spawn.play()

    def update(self, screen):
        sprite.Sprite.update(self, screen)

        """
        powerup update routine
        """
        self.__draw(screen)

    def check_collide(self, paddle, number):

        """
        check collision with paddle
        """

        if self.overlap(paddle):

            # okay, we have collide, now consequences
            if number > 0:
                self.level.build()
            else:
                self.level.shoot(paddle)
            return True

    def __draw(self, screen):

        """
        draw on screen each frame, and flicker
        """

        self.flicker_timer -= 1
        if self.flicker_timer < 5:
            pygame.draw.rect(screen, (200, 255, 255), (self.x, self.y, self.width, self.height))
        if self.flicker_timer == 0:
            self.flicker_timer = 10


__author__ = 'dj'
