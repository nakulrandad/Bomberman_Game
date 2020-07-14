import basics
import pygame
import random

random.seed(1)

class door:

    def __init__(self, door_img):
        self.img = door_img
        self.door_x = 80*random.randint(6,12)
        self.door_y = 40*(2*random.randint(1,4)+1)


    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()


    def draw(self, win):

        win.blit(self.img, (self.door_x, self.door_y))


