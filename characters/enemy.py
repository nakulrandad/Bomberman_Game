import random
import pygame
import basics


class Enemy:
    def __init__(self, x, y, enemy_img):
        self.x = x + 5 # for proper placement
        self.y = y + 5 # for proper placement
        self.img = enemy_img
        self.mask = pygame.mask.from_surface(enemy_img)
        self.life = 1
        self.vel = 1
        self.move_offset = 7
        self.mobility = [1,1,1,1] # UP, DOWN, LEFT, RIGHT

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def get_width(self):
        return self.img.get_width()
    
    def get_height(self):
        return self.img.get_height()

    def move(self):
        pass
        # if self.move_offset >= self.y%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE >= -self.move_offset:
        #     if keys[pygame.K_LEFT] and self.x - self.vel >= basics.BRICK_EDGE and self.mobility[2]: # left
        #         self.y -= (self.y%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE)
        #         self.x -= self.vel
        #     if keys[pygame.K_RIGHT] and self.x + self.vel + self.get_width() <= basics.WIDTH - basics.BRICK_EDGE and self.mobility[3]: # right
        #         self.y -= (self.y%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE)
        #         self.x += self.vel
        # if self.move_offset >= self.x%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE >= -self.move_offset:
        #     if keys[pygame.K_UP] and self.y - self.vel >= basics.BRICK_EDGE and self.mobility[0]: # up
        #         self.x -= self.x%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE
        #         self.y -= self.vel
        #     if keys[pygame.K_DOWN] and self.y + self.vel + self.get_height() <= basics.HEIGHT - basics.BRICK_EDGE and self.mobility[1]: # down
        #         self.x -= self.x%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE
        #         self.y += self.vel