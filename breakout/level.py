
# level object, containing bricks for player to smash and stage to play on


import brick
import pygame


class Level:

    def __init__(self):

        """
        New level, create array of bricks
        """

        self.bricks = list()
        self.__build()

    def __build(self):

        """
        Run two for loops to create wall of bricks
        """

        for x in xrange(0, 30):
            for y in xrange(0, 10):
                self.bricks.append(brick.Brick(x * 21 + 4, y * 6 + 4))

    def update(self, screen, ball):

        """
        Update screen background and draw bricks
        """

        screen.fill((0, 0, 0))
        pygame.draw.lines(screen, (200, 255, 200), False, [(0, 480), (0, 0), (639, 0), (639, 480)])
        [b.update(screen) for b in self.bricks]

        # and check for collisions in a copy of the list
        for i in self.bricks[:]:
            if i.overlap(ball):

                # we collided with ball, kill brick
                self.bricks.remove(i)
                ball.vy = -ball.vy
                ball.vx = -ball.vx
                ball.score = i.score


__author__ = 'dj'
