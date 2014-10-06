
import round

# instance of game class, containing objects like score, lives, etc....


class Game:

    def __init__(self, font):

        """
        new game instance
        """

        self.paused = False
        self.playing = True
        self.round = round.Round()
        self.timer = 240
        self.font = font

    def pause(self, screen):

        """
        pause game and display paused graphic
        """

        self.paused = True
        text = self.font.render("PAUSED", 0, (200, 255, 200), (0, 0, 0))
        screen.blit(text, (15, 100))

    def update(self, screen):

        """
        update current game instance
        """

        if not self.paused:
            self.round.update(screen)

            # occaisionally show word "boo"
            if self.round.boo > 0:
                self.round.boo -= 1
                text = self.font.render("Boo!", 0, (200, 255, 200))
                screen.fill((0, 0, 0))
                screen.blit(text, (300, 250))

            # show score onscreeen
            text = self.font.render(str(self.round.score), 0, (200, 255, 200))
            width = text.get_width()
            screen.blit(text, (600 - width, 400))

            # when the timer is at one, add ball to game
            if self.timer > 0:
                self.timer -= 1
                if self.timer == 169:
                    self.round.new_ball()
                if self.timer == 1:
                    self.round.ball.throw()
                if self.timer > 160:
                    text = self.font.render("BALLS REMAINING: " + str(self.round.lives), 0, (200, 255, 200), (0, 0, 0))
                    screen.blit(text, (15, 100))








__author__ = 'dj'
