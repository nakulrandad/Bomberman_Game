import basics
import pygame

class Player:
    def __init__(self, x, y, player_img):
        self.x = x
        self.y = y
        self.img = player_img
        self.mask = pygame.mask.from_surface(self.img)
        self.lives = 4
        self.vel = 10
        self.COOLDOWN = basics.FPS/2
        self.cooldown_counter = 0

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def get_width(self):
        return self.img.get_width()
    
    def get_height(self):
        return self.img.get_height()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x - self.vel > 0: # left
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x + self.vel + self.get_width() < basics.WIDTH: # right
            self.x += self.vel
        if keys[pygame.K_UP] and self.y - self.vel > 0: # up
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y + self.vel + self.get_height() + 15 < basics.HEIGHT: # down
            self.y += self.vel

    def cooldown(self): # Supposed to run every frame
        if self.cooldown_counter >= self.COOLDOWN:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

    def plant(self):
        if self.cooldown_counter == 0:
            # Plant the bomb
            self.cooldown_counter = 1
            pass
