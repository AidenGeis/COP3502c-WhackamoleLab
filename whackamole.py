import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        #
        mole_image = pygame.image.load("mole.png")
        x_mole,y_mole = 0, 0
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_mouse, y_mouse = event.pos
                    mouse_grid = (x_mouse//32, y_mouse//32)
                    mole_grid = (x_mole//32, y_mole//32)
                    if mouse_grid == mole_grid:
                        x_mole, y_mole = random.randrange(0,20)*32, random.randrange(0,16)*32

            screen.fill("light green")
            draw_lines(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(x_mole, y_mole)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


def draw_lines(screen):
    # vertical lines
    for i in range(1,20):
        pygame.draw.line(screen, 'dark green', ((i*32),0), ((i*32),512))
    for i in range(1,16):
        pygame.draw.line(screen, 'dark green', (0,(i*32)), (640,(i*32)))

if __name__ == "__main__":
    main()
