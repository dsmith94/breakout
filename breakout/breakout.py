
import game
import pygame
import registry
import sys


# new game instance
def start():

    """
    Create new instance of this game by calling sequence of startup functions
    """

    # create new registry object and boot
    reg = registry.Registry()
    __boot(reg)


def __events(reg):

    """
    check and handle events
    """

    # get player object
    player = reg.game.round.player

    # now check events
    for event in pygame.event.get():

        # get key events
        if event.type == pygame.KEYUP:

            # pause key
            if event.key == pygame.K_p:
                if reg.game.paused:
                    pygame.mixer.unpause()
                    reg.game.paused = False
                else:
                    pygame.mixer.stop()
                    sound = pygame.mixer.Sound('./breakout/pause.ogg')
                    sound.play()
                    reg.game.pause(reg.screen)

            # space key to restart when game is over
            if event.key == pygame.K_SPACE:

                if not reg.game.playing:
                    reg.game = None
                    pygame.mixer.stop()
                    reg.game = game.Game(reg.font)

        if event.type == pygame.KEYDOWN:

            # exit program on q
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # left key
            if event.key == pygame.K_LEFT:
                if player.left_paddle.x > 0:
                    player.left_paddle.mx = -10
                    player.right_paddle.mx = -10

            # right key
            if event.key == pygame.K_RIGHT:
                if player.right_paddle.x + player.right_paddle.width < reg.screen_width:
                    player.left_paddle.mx = 10
                    player.right_paddle.mx = 10

        if player.x < 0:
            player.x = 0
        if player.x > reg.screen_width - player.width:
            player.x = reg.screen_width - player.width

        # quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def __update(reg):

    """
    update routine, run once per frame
    """

    # game update
    reg.game.update(reg.screen)

    # check events
    __events(reg)

    # check if ball is off screen
    if reg.game.round.ball:
        __ball(reg)

    # game over text if game not playing
    if not reg.game.playing:
        text = reg.font.render("GAME OVER - SPACE TO RESTART", 0, (200, 255, 200), (0, 0, 0))
        reg.screen.blit(text, (15, 100))

    # update screen
    #__staticy(reg)
    pygame.display.flip()
    reg.clock.tick(50)


def __ball(reg):

    """
    Check if ball has fallen offscreen
    """

    if reg.game.round.ball.y > 480:

        # ball is lost, take away life
        reg.game.round.lives -= 1
        if reg.game.round.lives == 2:
            sound_music = pygame.mixer.Sound('./breakout/music.ogg')
            sound_music.play()

        # pause for a second with a timer if lives remain
        if reg.game.round.lives > 0:
            reg.game.timer = 300

        else:

            # game is over, we are out of lives
            reg.game.playing = False
            reg.game.round.level.shot = None
            reg.game.round.player.powerup = None
            reg.game.round.player.sound_gameover.play()

        # remove ball
        reg.game.round.ball = None


def __staticy(reg):

    """
    show static linieness on screen
    """

    line_counter = 0
    for y in xrange(reg.y_offset, 480):
        line_counter += 1
        if line_counter > 4:
            pygame.draw.aaline(reg.screen, (0, 0, 0), (0, y - 10), (reg.screen_width, y))
            pygame.draw.aaline(reg.screen, (0, 0, 0), (0, y - 9), (reg.screen_width, y))
            line_counter = 0
    reg.y_offset += 1
    if reg.y_offset > 4:
        reg.y_offset = 0


def __boot(reg):

    """
    Boot game by starting pygame init routines, run only once when game first boots
    """

    pygame.init()
    pygame.key.set_repeat(1, 1)
    reg.clock = pygame.time.Clock()
    reg.screen = pygame.display.set_mode(reg.screen_size, pygame.FULLSCREEN)
    reg.font = pygame.font.Font("./breakout/digiface.ttf", 40)
    reg.game = game.Game(reg.font)

    # begin loop
    while True:
        __update(reg)


__author__ = 'dj'
