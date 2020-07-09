import basics
import pygame
import random

random.seed(1)

class Br:

    def __init__(self, side_length, brwall_img):
        self.img = brwall_img
        self.side_l = side_length
        self.list = [[random.randint(0,1) for i in range(23)] for j in range(17)]

    def start_h(self):
        return 60

    def start_v(self):
        return 55

    def end_h(self):
        return 960

    def end_v(self):
        return 760

    def get_rows(self):
        return (int((960 - 60 + 40)/40))

    def get_cols(self):
        return (int((760 - 55)/40))

    #list = [[random.randint(0,1) for i in range( (int((960 - 60 + 40)/40)))] for j in range((int((760 - 55)/40)))]

    def rand_matrix(self):
        pass
    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()

    def draw(self, win):
        for i in range(self.get_rows()-12):
            for j in range(self.get_cols()-9):
                if self.list[j][i]:
                    win.blit(self.img, (80+80*i, 120 + 80*j))
