import basics
import pygame
import random

random.seed(1)

class Br:

    def __init__(self, side_length, brwall_img):
        self.img = brwall_img
        self.side_l = side_length
        self.list = [[random.randint(0,1) for i in range(23)] for j in range(19)]
        # self.list = [[0 for i in range(23)] for j in range(19)]
        for i in range(1,23,2):
            for j in range(1,19,2):
                self.list[j][i]=0
        for i in range(5):
            for j in range(5):
                self.list[i][j] = 0



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

    def destroy(self, iy,x):
        x  = round((x-40)/40)
        iy = round((iy-40)/40)
        #self.list = [[0 for i in range(11)] for j in range(8)]
        if x==0:
            if iy==0:
                self.list[x+1][iy]=0
                self.list[x][iy+1]=0
            elif iy==22:
                self.list[x + 1][iy] = 0
                self.list[x][iy - 1] = 0
            else:
                self.list[x][iy + 1] = 0
                self.list[x][iy - 1] = 0
                self.list[x + 1][iy] = 0

        elif x==18:
            if iy==0:
                self.list[x][iy]=0
                self.list[x][iy+1]=0
            elif iy==22:
                self.list[x -1][iy] = 0
                self.list[x][iy] = 0
            else:
                self.list[x - 1][iy] = 0
                self.list[x][iy] = 0
                self.list[x][iy + 1] = 0

        elif iy==22:
            self.list[x - 1][iy] = 0
            self.list[x][iy-1] = 0
            self.list[x+1][iy]=0

        elif iy==0:
            self.list[x - 1][iy] = 0
            self.list[x][iy +1] = 0
            self.list[x + 1][iy] = 0


        else:
            self.list[x + 1][iy] = 0
            self.list[x][iy + 1] = 0
            self.list[x - 1][iy] = 0
            self.list[x][iy-1] = 0


    def draw(self, win):
        for i in range(self.get_rows()):
            for j in range(self.get_cols()+2):
                if self.list[j][i]:
                    win.blit(self.img, (40+40*i, 40+40*j))

    def get_loc(self):
        loc = []
        for i in range(self.get_rows()):
            for j in range(self.get_cols()+2):
                if self.list[j][i]:
                    loc.append((40+40*i, 40+40*j))
        loc = list(set(loc)) # removes duplicates
        return loc
