
#
#   shot - to destroy bricks
#

import powerup


class Shot(powerup.Powerup):

    def __init__(self, paddle, level):
        powerup.Powerup.__init__(self, level)

        """
        make new shot
        """

        self.x = paddle.x + 10
        self.y = paddle.y
        self.vy = -10
        self.flicker_timer = -1

    def update(self, screen):
        powerup.Powerup.update(self, screen)

        """
        update shot on screen, check collision
        """

        for b in self.level.bricks:
            if self.overlap(b):
                self.level.bricks.remove(b)

__author__ = 'dj'
