import basics
import pygame


class Player:
    def __init__(self, x, y, player_img, bomb_img,Br_wall):
        self.x = x
        self.y = y
        self.img = player_img
        self.bomb = bomb_img
        self.bomb_small = pygame.transform.scale(bomb_img,(30,30))
        self.mask = pygame.mask.from_surface(player_img)
        self.lives = 4
        self.vel = 10
        self.COOLDOWN = basics.FPS*2
        self.cooldown_counter = 0
        self.bomb_x = 0
        self.bomb_y = 0
        self.Br_wall1 = Br_wall
        self.move_offset = 7
        self.mobility = [1,1,1,1] # UP, DOWN, LEFT, RIGHT

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def get_width(self):
        return self.img.get_width()
    
    def get_height(self):
        return self.img.get_height()

    def move(self):
        keys = pygame.key.get_pressed()

        # #tbr #move anywhere
        # if keys[pygame.K_LEFT] and self.x - self.vel >= basics.BRICK_EDGE: # left
        #         self.x -= self.vel
        # if keys[pygame.K_RIGHT] and self.x + self.vel + self.get_width() <= basics.WIDTH - basics.BRICK_EDGE: # right
        #         self.x += self.vel
        # if keys[pygame.K_UP] and self.y - self.vel >= basics.BRICK_EDGE: # up
        #         self.y -= self.vel
        # if keys[pygame.K_DOWN] and self.y + self.vel + self.get_height() <= basics.HEIGHT - basics.BRICK_EDGE: # down
        #         self.y += self.vel
        # #

        if self.move_offset >= self.y%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE >= -self.move_offset:
            if keys[pygame.K_LEFT] and self.x - self.vel >= basics.BRICK_EDGE and self.mobility[2]: # left
                self.y -= (self.y%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE)
                self.x -= self.vel
            if keys[pygame.K_RIGHT] and self.x + self.vel + self.get_width() <= basics.WIDTH - basics.BRICK_EDGE and self.mobility[3]: # right
                self.y -= (self.y%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE)
                self.x += self.vel
        if self.move_offset >= self.x%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE >= -self.move_offset:
            if keys[pygame.K_UP] and self.y - self.vel >= basics.BRICK_EDGE and self.mobility[0]: # up
                self.x -= self.x%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE
                self.y -= self.vel
            if keys[pygame.K_DOWN] and self.y + self.vel + self.get_height() <= basics.HEIGHT - basics.BRICK_EDGE and self.mobility[1]: # down
                self.x -= self.x%(basics.BRICK_EDGE*2) - basics.BRICK_EDGE
                self.y += self.vel
        # print("Player pos:", self.x, self.y) # tbr

    def cooldown(self, win): # Supposed to run every frame
        if self.cooldown_counter >= self.COOLDOWN:
            self.Br_wall1.destroy(self.bomb_x, self.bomb_y)
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            if (self.cooldown_counter/15)%2==1:
                win.blit(self.bomb, (self.bomb_x, self.bomb_y))
            else:
                win.blit(self.bomb, (self.bomb_x, self.bomb_y)) # yet to adjust blinking effect before bomb explodes

            self.cooldown_counter += 1

    def plant(self,win):
        keys = pygame.key.get_pressed()
        if self.cooldown_counter == 0 and keys[pygame.K_m]:
            # Plant the bomb
            win.blit(self.bomb, (self.x, self.y))
            self.bomb_x = round(self.x/40) * 40
            self.bomb_y = round(self.y/40) * 40
            self.cooldown_counter = 1
            print("Player pos:", self.x, self.y) # tbr
            print("Bomb pos:", self.bomb_x, self.bomb_y) # tbr
            
