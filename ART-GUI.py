import pygame
import sys


class Sim_board():
    def __init__(self,size,failurerate):
        self.size = size
        self.failure_rate = failurerate
        self.height = 800
        self.width = 600
        self.caption = "Task 1"
        self.background_colour = (255, 255, 255)

    def rungame(self):
        screen = pygame.display.set_mode((self.height, self.width))
        pygame.display.set_caption(self.caption)
        screen.fill(self.background_colour)
        pygame.display.flip()
        canvas = pygame.Surface((self.height, self.width))
        canvas.fill(self.background_colour)
        p1_camera = pygame.Rect(0, 0, self.height/2, self.width/2)
        p2_camera = pygame.Rect(self.height/2, 0, self.height/2, self.width/2)
        p3_camera = pygame.Rect(0, self.width/2, self.height/2, self.width/2)
        p4_camera = pygame.Rect(self.height/2, self.width/2, self.height/2, self.width/2)
        sub1 = canvas.subsurface(p1_camera)
        sub2 = canvas.subsurface(p2_camera)
        sub3 = canvas.subsurface(p3_camera)
        sub4 = canvas.subsurface(p4_camera)
        pygame.draw.line(sub2, (0, 0, 0), (0, 0), (0, self.width/2), 10)
        pygame.draw.line(sub3, (0, 0, 0), (0, 0), (self.height/2, 0), 10)
        pygame.draw.line(sub4, (0, 0, 0), (0, 0), (self.height/2, 0), 10)
        screen.blit(sub1, (0, 0))
        screen.blit(sub2, (self.height/2, 0))
        screen.blit(sub3, (0, self.width/2))
        screen.blit(sub4, (self.height/2, self.width/2))
        pygame.display.update()
        Flag = True
        while Flag:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Flag = False


run1=Sim_board(200,0.2)
run1.rungame()