import pygame
pygame.init()
pygame.font.init()
COLOR_INACTIVE = (125,125,125)
COLOR_ACTIVE = (0, 0, 0)
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



def run():
    screen = pygame.display.set_mode((640, 480))
    pygame.init()
    clock=pygame.time.Clock()
    label_sizex = Text("Size X:", 40, 100)
    label_sizey= Text("Size y:", 40, 150)
    label_trial=Text("No of Trial:", 40, 200)
    label_failure_rate=Text("failure rate:",40,250)
    input_sizex =InputBox(200,100,100,32,"400")
    input_sizey = InputBox(200, 150, 100, 32,"400")
    input_trial=InputBox(200,200,100,32,"0")
    input_failure_rate=InputBox(200,250,100,32,"0")
    labels=[label_sizex,label_sizey,label_trial,label_failure_rate]
    input_boxes=[input_sizex,input_sizey,input_trial,input_failure_rate]

    flag=True

    while flag:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                flag=False
            for input_box in input_boxes:
                input_box.handle_event(event)

        screen.fill((255,255,255))
        for inputbox in input_boxes:
            inputbox.draw(screen)
        for label in labels:
            label.draw(screen)
        pygame.display.flip()
        clock.tick(30)

run()
pygame.font.quit()
pygame.quit()

