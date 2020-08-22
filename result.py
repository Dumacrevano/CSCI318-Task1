import pygame

def result(ART_score,RT_score,Ties_score):
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    done = False


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()