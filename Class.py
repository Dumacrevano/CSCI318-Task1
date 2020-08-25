import pygame

pygame.init()
pygame.font.init()
COLOR_INACTIVE = (125,125,125)
COLOR_ACTIVE = (0, 0, 0)
LIGHT_GREEN= (0,255,0)
GREEN = (0,200,0)
My_font = pygame.font.SysFont("Comic Sans MS", 20)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = My_font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    # Re-render the text.
                self.txt_surface = My_font.render(self.text, True, self.color)

    def resize_box(self):
        width=max(200,self.txt_surface.get_width()+10)
        self.rect.w=width

    def draw(self,screen):
        screen.blit(self.txt_surface,(self.rect.x+5,self.rect.y+5))
        pygame.draw.rect(screen,self.color, self.rect,2)

class Text:
    def __init__(self,text,x,y):
        self.color = (0, 0, 0)
        self.x=x
        self.y=y
        self.rendered_txt=My_font.render(text, True, self.color)

    def draw(self,screen):
        screen.blit(self.rendered_txt,(self.x,self.y))

class Button:
    def __init__(self,light_color,dark_color,x,y,w,h,text):
        self.light_color=light_color
        self.dark_color=dark_color
        self.text=My_font.render(text,True,(255,255,255))
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def draw(self, screen,mouse):
        if self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y:
            pygame.draw.rect(screen, self.light_color, [self.x,self.y,self.w,self.h])
        else:
            pygame.draw.rect(screen, self.dark_color, [self.x,self.y,self.w,self.h])
        screen.blit(self.text,(self.x+5,self.y+5))
