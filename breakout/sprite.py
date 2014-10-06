
# sprite subsystem
# for paddle, ball and bricks


class Sprite():

    def __init__(self):

        """
        Create new instance of this sprite
        """

        self.x = 0
        self.y = 0

        # velocity
        self.vx = 0
        self.vy = 0

        # max speed - default ten pixels, common for most sprites
        self.max = 20

        # drag
        self.drag = 1

        # momentum
        self.mx = 0
        self.my = 0

        # last x and y
        self.lx = 0
        self.ly = 0

        # width and height
        self.width = 0
        self.height = 0

    def overlap(self, sprite):

        """
        Overlap current sprite with another, passed above
        """

        if sprite is None:
            return False

        return not (sprite.x > self.x + self.width or sprite.x + sprite.width < self.x or sprite.y > self.y +
                    self.height or sprite.y + sprite.height < self.y)

    def update(self, screen):

        """
        Update this sprite
        to be called each frame
        """

        # move sprite
        self.__move()

    def __move(self):

        """
        Move current object according to velocity, momentum and drag
        """

        # update last x and y
        self.lx = self.x
        self.ly = self.y

        # and update from move speed
        self.__velocity()

    def __velocity(self):

        """
        Deal with velocity and acceleration in a sprite
        """

        # prevent max speed limit from being exceeded
        if self.vx > 0:
            if self.vx > self.max:
                self.vx = self.max
            if self.vx < 0:
                if self.vx < -self.max:
                    self.vx = -self.max
        if self.vy > 0:
            if self.vy > self.max:
                self.vy = self.max
            if self.vy < 0:
                if self.vy < -self.max:
                    self.vy = -self.max

        # x
        if self.mx < 0:
            drag = self.drag
        else:
            drag = -self.drag
        if drag < 0:
            if self.mx - drag < 0:
                self.mx = 0
        if drag > 0:
            if self.mx + drag > 0:
                self.mx = 0
        if self.mx != 0:
            self.mx += drag
            self.x += self.mx
        if self.vx != 0:
            self.x += self.vx

        # y
        if self.my < 0:
            drag = self.drag
        else:
            drag = -self.drag
        if drag < 0:
            if self.my - drag < 0:
                self.my = 0
        if drag > 0:
            if self.my + drag > 0:
                self.my = 0
        if self.my != 0:
            self.my += drag
            self.y += self.my
        if self.vy != 0:
            self.y += self.vy


__author__ = 'dj'
