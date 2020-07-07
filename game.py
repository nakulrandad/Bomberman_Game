import pygame
import sys
import os
import random
pygame.init()


FPS = 60
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomberman")

# Load images
MAIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "green_grass.jpeg")), (WIDTH, HEIGHT))


def game_begin():
    run = True
    title_font = pygame.font.SysFont("comicsans", 60)
    while run:
        WIN.blit(MAIN_BG, (0,0))
        title_label = title_font.render("Press spacebar to start", 1, (0,0,255))
        WIN.blit(title_label, (int((WIDTH - title_label.get_width())/2), int(7/15 * HEIGHT)))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                sys.exit()
            if keys[pygame.K_SPACE]:
                pass
    # sys.exit()

if __name__ == "__main__":
    game_begin()