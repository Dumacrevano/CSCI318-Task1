import pygame
import simboard

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
        self.text=My_font.render(text,True,(0,0,0))
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





def run():
    screen = pygame.display.set_mode((640, 480))
    pygame.init()
    clock=pygame.time.Clock()

    button_start=Button(LIGHT_GREEN,GREEN,280,400,80,40,"START")

    label_sizex = Text("Size X:", 40, 100)
    label_sizey= Text("Size Y:", 40, 150)
    label_trial=Text("No of Trial:", 40, 200)
    label_failure_rate=Text("failure rate:",40,250)
    label_dumac=Text("No. of Candidate",40,300)
    input_sizex =InputBox(200,100,100,32,"400")
    input_sizey = InputBox(200, 150, 100, 32,"400")
    input_trial=InputBox(200,200,100,32,"100")
    input_failure_rate=InputBox(200,250,100,32,"0.2")
    input_candidate=InputBox(200,300,100,32,"10")
    labels=[label_sizex,label_sizey,label_trial,label_failure_rate,label_dumac]
    input_boxes=[input_sizex,input_sizey,input_trial,input_failure_rate,input_candidate]

    flag=True

    while flag:
        mouse = pygame.mouse.get_pos()
        screen.fill((255, 255, 255))
        button_start.draw(screen, mouse)

        for inputbox in input_boxes:
            inputbox.draw(screen)
        for label in labels:
            label.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            for input_box in input_boxes:
                input_box.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:  # check if mouse button is clicked
                if button_start.x + button_start.w > mouse[0] > button_start.x and button_start.y + button_start.h > mouse[1] > button_start.y:
                    txt_box_data=[]
                    for input_box in input_boxes:
                        txt_box_data.append(input_box.text)#get data from input boxes

                    flag=False
                    run1=simboard.Sim_board(int(txt_box_data[0]),int(txt_box_data[1]),
                                            int(txt_box_data[2]),float(txt_box_data[3]),int(txt_box_data[4]))#pass data to the simulation board
                    run1.rungame()




        pygame.display.flip()
        clock.tick(30)

run()
pygame.font.quit()
pygame.quit()

