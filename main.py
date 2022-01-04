import pygame
from pygame.locals import *
from rcaudio import *
import time
import logging

from random import randrange

class Mush:

    def __init__(self, surface):
        self.parent_screen = surface
        self.mush = pygame.image.load("resources/mush.png").convert()
        self.mush_x = randrange(500)
        self.mush_y = randrange(500)




    def draw(self):
        self.parent_screen.blit(self.mush, (self.mush_x, self.mush_y))


        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 700))
        self.surface.fill((125, 173, 250))  # rgb color
        pygame.display.flip()

        self.mush = Mush(self.surface)

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

        SR = SimpleRecorder()
        VA = VolumeAnalyzer(rec_time=1)
        SR.register(VA)
        SR.start()

        val = 0
        count = 1

        while (count < 3):

            count = count + 1
            abort_after = 3.0
            start = time.time()

            while True:

                delta = time.time() - start

                print("VOLUME : ", VA.get_volume())
                val = val + VA.get_volume()
                print("totVal:", val)
                time.sleep(1)

                if (val < 500):
                    self.mush.draw()
                    self.mush.draw()


                if delta >= abort_after:
                    break

            print("session " + str(count) + " session is over****")







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
