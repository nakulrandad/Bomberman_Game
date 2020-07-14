import random
import pygame
import basics


class Enemy:
    def __init__(self, x, y, enemy_img):
        self.x = x 
        self.y = y 
        self.img = enemy_img
        self.mask = pygame.mask.from_surface(enemy_img)
        self.life = 1
        self.vel = 1
        # self.move_offset = 7
        self.mobility = [0,0,0,0] # UP, DOWN, LEFT, RIGHT
        self.move_countdown = 0
        self.COUNTDOWN = basics.BRICK_EDGE * 4

    def draw(self, win):
        win.blit(self.img, (self.x + 4, self.y + 4)) # for proper placement

    def get_width(self):
        return self.img.get_width()
    
    def get_height(self):
        return self.img.get_height()

    def countdown(self):
        if self.move_countdown >= self.COUNTDOWN-1:
            self.move_countdown = 0
        elif self.move_countdown >= 0:
            self.move_countdown += 1

    def move(self):
        self.countdown()
        if self.move_countdown == 1:
            self.x = round(self.x/40) * 40
            self.y = round(self.y/40) * 40
            if self.mobility[0] == 0: # Can't go up
                self.mobility = [0,0,0,0]
                self.mobility[random.choice([1,2,3])] = 1
            if self.mobility[1] == 0: # Can't go down
                self.mobility = [0,0,0,0]
                self.mobility[random.choice([0,2,3])] = 1
            if self.mobility[2] == 0: # Can't go left
                self.mobility = [0,0,0,0]
                self.mobility[random.choice([0,2,3])] = 1
            if self.mobility[3] == 0: # Can't go right
                self.mobility = [0,0,0,0]
                self.mobility[random.choice([0,1,2])] = 1
            print(self.x, self.y, "Enemy loc")
        if self.x - self.vel >= basics.BRICK_EDGE and self.mobility[2]: # left
            # self.y -= (self.y%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE)
            self.x -= self.vel
        if self.x + self.vel + self.get_width() <= basics.WIDTH - basics.BRICK_EDGE and self.mobility[3]: # right
            # self.y -= (self.y%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE)
            self.x += self.vel
        if self.y - self.vel >= basics.BRICK_EDGE and self.mobility[0]: # up
            # self.x -= self.x%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE
            self.y -= self.vel
        if self.y + self.vel + self.get_height() <= basics.HEIGHT - basics.BRICK_EDGE and self.mobility[1]: # down
            # self.x -= self.x%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE
            self.y += self.vel