import basics
import pygame
import os
from characters.player import Player
WIN = basics.WIN

# Player images
PLAYER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_img", "balloon_nobg.png")), (40,40))

# Brick images
RED_BRICK = pygame.transform.scale(pygame.image.load(os.path.join("assets", "brick_img", "red_brick_nobg.png")), (10,10))
GREY_BRICK = pygame.transform.scale(pygame.image.load(os.path.join("assets", "brick_img", "grey_brick_nobg.png")), (10,10))
WHITE_BRICK = pygame.transform.scale(pygame.image.load(os.path.join("assets", "brick_img", "white_brick.jpeg")), (10,10))

# Background images
BG = []
BG.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "grass.jpeg")), (basics.WIDTH, basics.HEIGHT)))
BG.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "yellow_sand.png")), (basics.WIDTH, basics.HEIGHT)))
BG.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "snow.jpg")), (basics.WIDTH, basics.HEIGHT)))

# Bomb images
BOMB = pygame.image.load(os.path.join("assets", "bomb_img", "bomb_nobg.png"))

def main():
    run = True
    clock = pygame.time.Clock()
    bg_num = 0

    players = []

    player1 = Player( basics.WIDTH/2 , basics.HEIGHT/2 , PLAYER)
    players.append(player1)

    def redraw_window():
        WIN.blit(BG[bg_num], (0,0))
        for player in players:
            player.draw(WIN)
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
        
