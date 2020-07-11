import basics
import pygame
import os
from characters.player import Player
from characters.enemy import Enemy
from Walls.Unbreakable import Unbr
from Walls.Breakable import Br
WIN = basics.WIN

# Player images
PLAYER = pygame.transform.scale(pygame.image.load(os.path.join("assets", "player_img", "balloon_nobg.png")), (42,42))

# Enemy images
BLINKY = pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_img", "blinky_nobg.png")), (32,32))
PINKY = pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_img", "pinky_nobg.png")), (32,32))
INKY = pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_img", "inky_nobg.png")), (32,32))
CLYDE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_img", "clyde_nobg.png")), (32,32))
ENEMIES = [BLINKY, PINKY, INKY, CLYDE]

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
    unbr_wall = Unbr(40,RED_BRICK)
    Br_wall = Br(40,WHITE_BRICK)
    player1 = Player(basics.BRICK_EDGE, basics.BRICK_EDGE, PLAYER, BOMB, Br_wall)
    # #tbr
    # print(Br_wall.get_loc())
    # #

    players.append(player1)

    def collide(obj1, obj2):
        offset_x = int(obj2.x - obj1.x)
        offset_y = int(obj2.y - obj1.y)
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    def wall_detection(obj):
        pass

    def redraw_window():
        WIN.blit(BG[bg_num], (0,0))
        for player in players:
            player.draw(WIN)
            player.plant(WIN)
            player.cooldown(WIN)
        # enemy1.draw(WIN)
        unbr_wall.draw(WIN)
        Br_wall.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(basics.FPS)
        redraw_window()

        brick_locs = Br_wall.get_loc()

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
            # tbr
            if pygame.mouse.get_pressed() == (1,0,0):
                print("Mouse pos", pygame.mouse.get_pos())
            #
        for player in players:
            for loc in brick_locs:
                if (loc[0]-3+basics.BRICK_EDGE<=player.x<loc[0]+basics.BRICK_EDGE)and(loc[1]<=player.y<loc[1]+basics.BRICK_EDGE):
                    player.mobility = [1,1,0,1]
                    print("Can't move left")
                if (loc[0]-basics.BRICK_EDGE<player.x<=loc[0]+3-basics.BRICK_EDGE)and(loc[1]<=player.y<loc[1]+basics.BRICK_EDGE):
                    player.mobility = [1,1,1,0]
                    print("Can't move right")
                if (loc[1]-3+basics.BRICK_EDGE<=player.y<loc[1]+basics.BRICK_EDGE)and(loc[0]<=player.x<loc[0]+basics.BRICK_EDGE):
                    player.mobility = [0,1,1,1]
                    print("Can't move up", player.x, player.y)
                if (loc[1]-basics.BRICK_EDGE<player.y<=loc[1]+3-basics.BRICK_EDGE)and(loc[0]<=player.x<loc[0]+basics.BRICK_EDGE):
                    player.mobility = [1,0,1,1]
                    print("Can't move down")
            player.move()
            player.mobility = [1,1,1,1] # UP, DOWN, LEFT, RIGHT
        
