from  constants import *
import pygame
from Conway import Conway

def main():
    pygame.init()
    pygame.display.set_caption("Mini Project - Conway's Game Of Life")
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    CGoL = Conway(width,height, scaler, offset)

    running = True
    while running:
        clock.tick(fps)
        screen.fill(blue)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    CGoL.togglePause()
        CGoL.evolve(off_color=black, on_color=white, surface=screen)
        if not CGoL.pause:
            CGoL.update()

        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            CGoL.handleMouse(mouseX, mouseY)

        pygame.display.update()

    pygame.quit()


main()