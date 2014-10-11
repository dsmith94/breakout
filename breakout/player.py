

import sprite
import pygame


# instance of current player paddle


class Paddle(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)

        """
        Create new paddle instance - actually two paddles mashed together
        """

        self.width = 100
        self.height = 5
        self.drag = 5
        self.timer = 0
        self.flicker = 0
        self.left_paddle = sprite.Sprite()
        self.right_paddle = sprite.Sprite()
        self.left_paddle.x = 10
        self.left_paddle.y = 440
        self.right_paddle.y = 440
        self.left_paddle.width = 50
        self.right_paddle.width = 50
        self.right_paddle.x = self.left_paddle.x + self.left_paddle.width
        self.left_paddle.max = 15
        self.right_paddle.max = 15
        self.left_paddle.height = 5
        self.right_paddle.height = 5
        self.split_timer = 0
        self.number_of_powerups = 0
        self.powerup = None
        self.shot = None

        # sound effects
        self.sound_gameover = pygame.mixer.Sound('./breakout/gameover.ogg')
        self.sound_powerup = pygame.mixer.Sound('./breakout/powerup.ogg')
        self.sound_bounce = pygame.mixer.Sound('./breakout/bounce.ogg')
        self.sound_rebuild = pygame.mixer.Sound('./breakout/rebuild.ogg')
        self.sound_open = pygame.mixer.Sound('./breakout/open.ogg')
        self.sound_shrink = pygame.mixer.Sound('./breakout/shrink.ogg')
        self.sound_heal = pygame.mixer.Sound('./breakout/heal.ogg')

    def shrink(self):

        """
        run timer for shrink
        """

        self.timer = 100
        self.left_paddle.x += 30
        self.left_paddle.width = 20
        self.right_paddle.width = 20
        self.sound_shrink.play()

    def split(self):

        """
        split paddle in two
        """

        self.split_timer = 30
        self.sound_open.play()

    def update(self, screen):
        sprite.Sprite.update(self, screen)

        # handle split timer
        if self.split_timer > 0:
            self.split_timer -= 1
            if self.split_timer > 15:
                self.left_paddle.mx = -5
                self.right_paddle.mx = 5
            if self.split_timer < 15:
                self.left_paddle.vx = 5
                self.right_paddle.vx = -5
            if self.split_timer == 0:
                self.left_paddle.vx = 0
                self.right_paddle.vx = 0
                self.right_paddle.x = self.left_paddle.x + self.left_paddle.width

        # handle shrink prank
        if self.timer > 0:
            self.timer -= 1
            if self.timer == 1:
                self.sound_heal.play()
                self.left_paddle.x -= 30
                self.left_paddle.width = 50
                self.right_paddle.width = 50

        # update powerup
        if self.powerup:
            self.powerup.update(screen)
            if self.powerup.check_collide(self.left_paddle, self.number_of_powerups):
                self.number_of_powerups += 1
                self.powerup = None
                if self.number_of_powerups == 1:
                    self.sound_powerup.play()
                else:
                    self.sound_rebuild.play()
            elif self.powerup.check_collide(self.right_paddle, self.number_of_powerups):
                self.number_of_powerups += 1
                self.powerup = None
                if self.number_of_powerups == 1:
                    self.sound_powerup.play()
                else:
                    self.sound_rebuild.play()

        # update sub paddles
        self.left_paddle.update(screen)
        self.right_paddle.update(screen)

        # draw sprite
        if self.flicker == 0:
            self.__draw(screen)
        else:
            self.flicker -= 1

    def __draw(self, screen):

        """
        Draw paddle on screen
        """

        pygame.draw.rect(screen, (200, 255, 200), (self.left_paddle.x, self.left_paddle.y, self.left_paddle.width,
                                                   self.left_paddle.height))
        pygame.draw.rect(screen, (200, 255, 200), (self.right_paddle.x, self.right_paddle.y, self.right_paddle.width,
                                                   self.right_paddle.height))


__author__ = 'dj'
