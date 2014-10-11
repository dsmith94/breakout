
# each life of the player is a round
# define round data here

import player
import powerup
import level
import ball
import random
import pygame


class Round:

    def __init__(self):

        """
        Define new round
        """

        self.player = player.Paddle()
        self.level = level.Level()
        self.lives = 3
        self.ball = None
        self.score = 0
        self.boo = 0
        self.timer = 500
        self.scorekiller = 0
        self.score_to_remove = 0

        # sound effects
        self.sound_score = pygame.mixer.Sound('./breakout/score.ogg')
        self.sound_jump = pygame.mixer.Sound('./breakout/jump.ogg')

    def new_ball(self):

        """
        New ball on screen
        """

        self.ball = ball.Ball()
        self.ball.x = 200 * random.random()
        self.ball.y = 200 * random.random()
        self.ball.y += 200

    def prank(self):

        """
        randomly prank player
        """

        # prank time! mess with player
        if self.scorekiller == 0 and self.score_to_remove > 0:
            self.score -= 1
            self.score_to_remove -= 1
            self.scorekiller = 30
            self.sound_score.play()
        if self.scorekiller > 0:
            self.scorekiller -= 1
        if self.timer > 0:
            self.timer -= 1
        if self.timer == 0:
            if self.ball:
                if self.ball.vy > 0:
                    if self.ball.y > 400:
                        p = int((random.random() * 17))
                        if p == 1:
                            self.boo = 10
                        if p == 2:
                            self.player.shrink()
                        if p == 3:
                            self.ball.my = -20
                            self.sound_jump.play()
                        if p == 4:
                            self.player.flicker = 30
                        if p == 5:
                            self.score_to_remove = 10
                        if p == 6:
                            self.player.split()
                        if p == 7:
                            self.player.powerup = powerup.Powerup(self.level)
                        if p < 8:
                            self.timer = 200

    def update(self, screen):

        """
        Update current round
        """

        self.level.update(screen, self.ball)
        if self.ball:
            if self.ball.score > 0:
                self.score += self.ball.score
            self.ball.update(screen, self.player)
        self.player.update(screen)
        self.prank()


__author__ = 'dj'
