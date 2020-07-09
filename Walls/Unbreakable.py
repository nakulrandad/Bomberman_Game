import basics
import pygame

class Unbr:
    def __init__(self, side_length ,unbrwall_img):
        self.img = unbrwall_img
        self.side_l = side_length
    def get_width(self):
        return self.img.get_width()
    
    def get_height(self):
        return self.img.get_height()

    def draw(self, win):
        for i in range(20,1000,40):
            win.blit(self.img,(i,0))
        for i in range(20, 1000, 40):
            win.blit(self.img, (i, 760))
        for i in range(0,800,40):
            win.blit(self.img,(0,i))
        for i in range(0,800,40):
            win.blit(self.img,(960,i))
        for i in range(80,920, self.side_l + self.get_width()):
            for j in range(80,760, self.side_l + self.get_height()):
                win.blit(self.img,(i,j))

