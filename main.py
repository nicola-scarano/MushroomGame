import pygame
from pygame.locals import *
from rcaudio import *
import time
import logging

from random import randrange

class Mush:

    def __init__(self, surface, m_x, m_y):
        self.mush_x = m_x
        self.mush_y = m_y
        self.parent_screen = surface

        self.mush = pygame.image.load("resources/mush.png").convert_alpha()

        color = 125, 173, 250
        self.mush.set_colorkey(color)



        self.land = pygame.image.load("resources/land1.jpg").convert()
        self.parent_screen.blit(self.land, (80, 325))




    def drawSadMush(self):
        sadMush = pygame.image.load("resources/indir.jfif").convert()
        self.parent_screen.blit(sadMush, (150, 250))
        pygame.display.flip()


    def draw(self):
        # mush location display
        self.parent_screen.blit(self.mush, (self.mush_x, self.mush_y))




        pygame.display.flip()


        self.mush_x =  randrange(200,900,15)
        self.mush_y = 565


class Game:
    def __init__(self):
        #icon-logo
        pygame.display.set_caption("MushGame")
        icon = pygame.image.load('resources/mush-logo.png')
        pygame.display.set_icon(icon)


        pygame.init()
        self.surface = pygame.display.set_mode((1100, 700))
        self.surface.fill((125, 173, 250))  # rgb color




        pygame.display.flip()

        self.mush_x = 650
        self.mush_y = 0

        self.mush = Mush(self.surface, self.mush_x, self.mush_y)

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

        SR = SimpleRecorder()
        VA = VolumeAnalyzer(rec_time=1)
        SR.register(VA)
        SR.start()

        val = 0
        count = 1

        score = 0

        while (count < 20):

            count = count + 1
            abort_after = 2.0 #5 sec
            start = time.time()


            while True:

                delta = time.time() - start

                print("VOLUME : ", VA.get_volume())
                val = val + VA.get_volume()
                print("totVal:", val)
                time.sleep(1)



                if delta >= abort_after:
                    break

            print("session " + str(count) + " session is over****")
            if (val < 650):

                myfont = pygame.font.SysFont("Goudy Stout", 28)

                placeholder = myfont.render(" " + str(score-1), True, (125, 173, 250))
                self.surface.blit(placeholder, (1009, 0))
                placeholder1 = myfont.render(" " + str(score-1), True, (125, 173, 250))
                self.surface.blit(placeholder1, (1008, 0))

                scoretext = myfont.render("# of Mush: " + str(score), True, (180, 240, 200))
                self.surface.blit(scoretext, (720, 0))
                self.mush.draw()

                score = score + 1

                print("mush drawn")
        if (score < 3):
            self.mush.drawSadMush()




    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.type == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False


if __name__ == '__main__':
    game = Game()
    game.run()
