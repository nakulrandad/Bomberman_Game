import basics
import pygame
import os
from characters.player import Player
from Walls.Unbreakable import Unbr
from Walls.Breakable import Br
WIN = basics.WIN

# Player images
PLAYER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_img", "balloon_nobg.png")), (42,42))
# Brick images
RED_BRICK = pygame.transform.scale(pygame.image.load(os.path.join("assets", "brick_img", "red_brick_nobg_noborders.png")), (40,40))
GREY_BRICK = pygame.transform.scale(pygame.image.load(os.path.join("assets", "brick_img", "grey_brick_nobg.png")), (40,40))
WHITE_BRICK = pygame.transform.scale(pygame.image.load(os.path.join("assets", "brick_img", "white_brick.jpeg")), (40,40))

# Background images
BG = []
BG.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "grass.jpeg")), (basics.WIDTH, basics.HEIGHT)))
BG.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "yellow_sand.png")), (basics.WIDTH, basics.HEIGHT)))
BG.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "snow.jpg")), (basics.WIDTH, basics.HEIGHT)))

# Bomb images
BOMB = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomb_img", "bomb_nobg.png")),(40,40))

def main():
    run = True
    clock = pygame.time.Clock()
    bg_num = 0

    players = []

    player1 = Player( basics.BRICK_EDGE , basics.BRICK_EDGE , PLAYER, BOMB)
    unbr_wall = Unbr(40,RED_BRICK)
    Br_wall = Br(40,WHITE_BRICK)
    players.append(player1)

    def redraw_window():
        WIN.blit(BG[bg_num], (0,0))
        for player in players:
            player.draw(WIN)
            player.plant(WIN)
            player.cooldown(WIN)
        unbr_wall.draw(WIN)
        Br_wall.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(basics.FPS)
        redraw_window()

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False

        for player in players:
            player.move()
        
