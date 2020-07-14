import basics
import pygame
import random

random.seed(1)

class key:

    def __init__(self, door_img):
        self.img = door_img
        self.key_x = 80*random.randint(3,6)
        self.key_y = 40*(2*random.randint(5,9)+1)
        self.not_collected = True


    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()


    def draw(self, win):
        if self.not_collected:
            win.blit(self.img, (self.key_x, self.key_y))


