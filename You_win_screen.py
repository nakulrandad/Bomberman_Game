import basics
import pygame
import os


# Background image

MAIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "yellow_sand.png")), (basics.WIDTH, basics.HEIGHT))


def you_win_screen():
    title_font = pygame.font.SysFont("comicsans", 60)
    basics.WIN.blit(MAIN_BG, (0, 0))
    title_label = title_font.render("You win!! The game will start in 5 seconds", 1, (0, 0, 255))
    basics.WIN.blit(title_label,
                    (int((basics.WIDTH - title_label.get_width()) / 2), int(7 / 15 * basics.HEIGHT)))
    pygame.display.update()
    pygame.time.wait(1000)
    basics.WIN.blit(MAIN_BG, (0, 0))
    title_label = title_font.render("You win!! The game will start in 4 seconds", 1, (0, 0, 255))
    basics.WIN.blit(title_label,
                    (int((basics.WIDTH - title_label.get_width()) / 2), int(7 / 15 * basics.HEIGHT)))
    pygame.display.update()
    pygame.time.wait(1000)
    basics.WIN.blit(MAIN_BG, (0, 0))
    title_label = title_font.render("You win!! The game will start in 3 seconds", 1, (0, 0, 255))
    basics.WIN.blit(title_label,
                    (int((basics.WIDTH - title_label.get_width()) / 2), int(7 / 15 * basics.HEIGHT)))
    pygame.display.update()
    pygame.time.wait(1000)
    basics.WIN.blit(MAIN_BG, (0, 0))
    title_label = title_font.render("You win!! The game will start in 2 seconds", 1, (0, 0, 255))
    basics.WIN.blit(title_label,
                    (int((basics.WIDTH - title_label.get_width()) / 2), int(7 / 15 * basics.HEIGHT)))
    pygame.display.update()
    pygame.time.wait(1000)
    basics.WIN.blit(MAIN_BG, (0, 0))
    title_label = title_font.render("You win!! The game will start in 1 seconds", 1, (0, 0, 255))
    basics.WIN.blit(title_label,
                    (int((basics.WIDTH - title_label.get_width()) / 2), int(7 / 15 * basics.HEIGHT)))
    pygame.display.update()
    pygame.time.wait(1000)
