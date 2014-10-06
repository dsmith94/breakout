
# the registry - a global object used for a few basic variables


class Registry():

    def __init__(self):

        """
        Init new registry object - this is done only once
        """

        self.clock = None
        self.game = None
        self.screen = None
        self.font = None
        self.black = (0, 0, 0)
        self.white = (200, 255, 200)
        self.screen_width = 640
        self.screen_height = 480
        self.screen_size = (self.screen_width, self.screen_height)
        self.y_offset = 0

    def restart(self):

        """
        restart game
        """



__author__ = 'dj'
