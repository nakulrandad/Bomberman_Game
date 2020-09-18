import basics
import pygame
import os
import random
from characters.player import Player
from characters.enemy import Enemy
from Walls.Unbreakable import Unbr
from Walls.Breakable import Br
from door_and_key.door import door
from door_and_key.key import key
from Game_over_screen import game_over_screen
from You_win_screen import you_win_screen


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
MAIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "yellow_sand.png")), (basics.WIDTH, basics.HEIGHT))

# Bomb images
BOMB = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bomb_img", "bomb_nobg.png")),(40,40))

#Door_Key image
DOOR = pygame.transform.scale(pygame.image.load(os.path.join("assets", "door_key_img", "door.png")),(40,40))
KEY = pygame.transform.scale(pygame.image.load(os.path.join("assets", "door_key_img", "key.png")),(40,40))

def main():
    run = True
    clock = pygame.time.Clock()
    bg_num = 0
    level = 1
    trigger_level = True
    players = []
    unbr_wall = Unbr(40,RED_BRICK)
    Br_wall = Br(40,WHITE_BRICK)
    player1 = Player(basics.BRICK_EDGE, basics.BRICK_EDGE, PLAYER, BOMB, Br_wall)
    Door = door(DOOR)
    Key = key(KEY)
    enemies = []

    #tbr
    # print(Br_wall.get_loc())
    #


    def collide(obj1, obj2):
        offset_x = int(obj2.x - obj1.x)
        offset_y = int(obj2.y - obj1.y)
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    def wall_detection(obj):
        pass

    def redraw_window():
        WIN.blit(BG[bg_num], (0,0))

        # enemy1.draw(WIN)
        Door.draw(WIN)
        Key.draw(WIN)

        unbr_wall.draw(WIN)
        Br_wall.draw(WIN)

        for enemy in enemies:
            for player in players:
                if enemy.kill(player.bomb_x, player.bomb_y, player.cooldown_counter):
                    enemies.remove(enemy)
            enemy.draw(WIN)

        for player in players:
            player.draw(WIN)
            player.plant(WIN)
            player.cooldown(WIN)
            if player.Player_kill(player.cooldown_counter):
                game_over_screen()
                return False
            if player.exit_door(WIN,Key,Door.door_x,Door.door_y):
                you_win_screen()
                return False

        pygame.display.update()
        return True

    while run:
        clock.tick(basics.FPS)

        if trigger_level == True:
            players = []
            enemies = []
            unbr_wall = Unbr(40,RED_BRICK)
            Br_wall = Br(40,WHITE_BRICK)
            player1 = Player(basics.BRICK_EDGE, basics.BRICK_EDGE, PLAYER, BOMB, Br_wall)
            players.append(player1)

            brick_locs = Br_wall.get_loc() # reset later
            for x in range(1, int(basics.WIDTH/basics.BRICK_EDGE - 2), 2):
                for y in range(1, int(basics.HEIGHT/basics.BRICK_EDGE - 2), 2):
                    i = x*basics.BRICK_EDGE + basics.BRICK_EDGE
                    j = y*basics.BRICK_EDGE + basics.BRICK_EDGE
                    brick_locs.append((i,j))

            for i in range(3 + round(level*1.5)):
                pos_x = random.choice(range(basics.BRICK_EDGE, basics.WIDTH - basics.BRICK_EDGE, 40))
                pos_y = random.choice(range(basics.BRICK_EDGE, basics.HEIGHT - basics.BRICK_EDGE, 40))
                while (pos_x, pos_y) in brick_locs:
                    pos_x = random.choice(range(basics.BRICK_EDGE, basics.WIDTH - basics.BRICK_EDGE, 40))
                    pos_y = random.choice(range(basics.BRICK_EDGE, basics.HEIGHT - basics.BRICK_EDGE, 40))
                enemies.append(Enemy(pos_x, pos_y, ENEMIES[i%4]))
            trigger_level = False


        if not redraw_window():
            run = False

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
            # tbr
            if pygame.mouse.get_pressed() == (1,0,0):
                print("Mouse pos", pygame.mouse.get_pos())
            #
        
        brick_locs = Br_wall.get_loc() # reset later    
        for player in players:
            for loc in brick_locs:
                if (loc[0]-3+basics.BRICK_EDGE<=player.x<loc[0]+basics.BRICK_EDGE)and(loc[1]<=player.y<loc[1]+basics.BRICK_EDGE):
                    player.mobility[2] = 0
                    # print("Can't move left")
                if (loc[0]-basics.BRICK_EDGE<player.x<=loc[0]+3-basics.BRICK_EDGE)and(loc[1]<=player.y<loc[1]+basics.BRICK_EDGE):
                    player.mobility[3] = 0
                    # print("Can't move right")
                if (loc[1]-3+basics.BRICK_EDGE<=player.y<loc[1]+basics.BRICK_EDGE)and(loc[0]<=player.x<loc[0]+basics.BRICK_EDGE):
                    player.mobility[0] = 0
                    # print("Can't move up")
                if (loc[1]-basics.BRICK_EDGE<player.y<=loc[1]+3-basics.BRICK_EDGE)and(loc[0]<=player.x<loc[0]+basics.BRICK_EDGE):
                    player.mobility[1] = 0
                    # print("Can't move down")
            player.move()
            player.mobility = [1,1,1,1] # UP, DOWN, LEFT, RIGHT

        for x in range(1, int(basics.WIDTH/basics.BRICK_EDGE - 2), 2):
            for y in range(1, int(basics.HEIGHT/basics.BRICK_EDGE - 2), 2):
                i = x*basics.BRICK_EDGE + basics.BRICK_EDGE
                j = y*basics.BRICK_EDGE + basics.BRICK_EDGE
                brick_locs.append((i,j))
        for player in players:
            brick_locs.append((player.bomb_x, player.bomb_y)) 
        for enemy in enemies:
            for loc in brick_locs:
                if (loc[0]-2+basics.BRICK_EDGE<=enemy.x<loc[0]+basics.BRICK_EDGE)and(loc[1]<=enemy.y<loc[1]+basics.BRICK_EDGE):
                    enemy.mobility[2] = 0
                    # print("Can't move left")
                if (loc[0]-basics.BRICK_EDGE<enemy.x<=loc[0]+2-basics.BRICK_EDGE)and(loc[1]<=enemy.y<loc[1]+basics.BRICK_EDGE):
                    enemy.mobility[3] = 0
                    # print("Can't move right")
                if (loc[1]-2+basics.BRICK_EDGE<=enemy.y<loc[1]+basics.BRICK_EDGE)and(loc[0]<=enemy.x<loc[0]+basics.BRICK_EDGE):
                    enemy.mobility[0] = 0
                    # print("Can't move up")
                if (loc[1]-basics.BRICK_EDGE<enemy.y<=loc[1]+2-basics.BRICK_EDGE)and(loc[0]<=enemy.x<loc[0]+basics.BRICK_EDGE):
                    enemy.mobility[1] = 0
                    # print("Can't move down")
                # if (loc[0]+basics.BRICK_EDGE==enemy.x)and(loc[1]<=enemy.y<loc[1]+basics.BRICK_EDGE):
                #     enemy.mobility[2] = 0
                #     # print("Can't move left")
                # if (loc[0]-basics.BRICK_EDGE==enemy.x)and(loc[1]<=enemy.y<loc[1]+basics.BRICK_EDGE):
                #     enemy.mobility[3] = 0
                #     # print("Can't move right")
                # if (loc[1]+basics.BRICK_EDGE==enemy.y)and(loc[0]<=enemy.x<loc[0]+basics.BRICK_EDGE):
                #     enemy.mobility[0] = 0
                #     # print("Can't move up")
                # if (loc[1]-basics.BRICK_EDGE==enemy.y)and(loc[0]<=enemy.x<loc[0]+basics.BRICK_EDGE):
                #     enemy.mobility[1] = 0
                #     # print("Can't move down")
            enemy.move()



            for player in players:
                if collide(player, enemy):
                    print("U r so dead!")
                    game_over_screen()
                    run = False

if __name__ == "__main__":
    main()
