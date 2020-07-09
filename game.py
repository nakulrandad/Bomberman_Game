import pygame
import sys
import os
import main
import basics


pygame.init()
pygame.display.set_caption("Bomberman")

# Load images
MAIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_img", "yellow_sand.png")), (basics.WIDTH, basics.HEIGHT))


def game_begin():
    run = True
    title_font = pygame.font.SysFont("comicsans", 60)
    while run:
        basics.WIN.blit(MAIN_BG, (0,0))
        title_label = title_font.render("Press spacebar to start", 1, (0,0,255))
        basics.WIN.blit(title_label, (int((basics.WIDTH - title_label.get_width())/2), int(7/15 * basics.HEIGHT)))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if keys[pygame.K_SPACE]:
                main.main()
    # sys.exit()

if __name__ == "__main__":
    game_begin()