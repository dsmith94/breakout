
# level object, containing bricks for player to smash and stage to play on


import brick
import pygame
import shot
import ghost


class Level:

    def __init__(self):

        """
        New level, create array of bricks
        """

        self.bricks = list()
        self.ghosts = list()
        self.build()
        self.shot = None
        self.sound_start = pygame.mixer.Sound('./breakout/start.ogg')
        self.sound_brick = pygame.mixer.Sound('./breakout/brick.ogg')
        self.sound_start.play()

    def build(self):

        """
        Run two for loops to create wall of bricks
        """

        self.bricks = list()
        for x in xrange(0, 15):
            for y in xrange(0, 5):
                self.bricks.append(brick.Brick(x * 41 + 12, y * 11 + 4))

    def shoot(self, paddle):

        """
        make new shot, from paddle
        """

        self.shot = shot.Shot(paddle, self)

    def update(self, screen, ball):

        """
        Update screen background and draw bricks
        """

        screen.fill((0, 0, 0))
        pygame.draw.lines(screen, (200, 255, 200), False, [(0, 480), (0, 0), (639, 0), (639, 480)])
        [b.update(screen) for b in self.bricks]
        for g in self.ghosts:
            g.update(screen)
            if g.timer < 1:
                self.ghosts.remove(g)

        # update shot
        if self.shot:
            self.shot.update(screen)
            if self.shot.y < -20:
                self.shot = None

        # and check for collisions in a copy of the list
        for i in self.bricks[:]:
            if i.overlap(ball):

                # we collided with ball, kill brick
                g = ghost.Ghost(i.x, i.y)
                self.bricks.remove(i)
                self.sound_brick.play()
                self.ghosts.append(g)
                ball.vy = -ball.vy
                ball.vx = -ball.vx
                ball.score = i.score


__author__ = 'dj'
