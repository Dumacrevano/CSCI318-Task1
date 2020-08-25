import pygame
from simboard import Sim_board
from Class import Text,InputBox, Button
pygame.init()
pygame.font.init()
COLOR_INACTIVE = (125,125,125)
COLOR_ACTIVE = (0, 0, 0)
LIGHT_GREEN= (0,255,0)
GREEN = (0,200,0)
My_font = pygame.font.SysFont("Comic Sans MS", 20)

def run():
    screen = pygame.display.set_mode((640, 480))
    pygame.init()
    clock=pygame.time.Clock()

    start_button = Button(LIGHT_GREEN, GREEN, 280, 400, 80, 40,"START")


    label_sizex = Text("Size X:", 40, 100)
    label_sizey= Text("Size Y:", 40, 150)
    label_trial = Text("No of Trial:", 40, 200)
    label_failure_rate = Text("failure rate:",40,250)
    label_dumac= Text("No. of Candidate",40,300)
    input_sizex = InputBox(200,100,100,32,"400")
    input_sizey = InputBox(200, 150, 100, 32,"400")
    input_trial = InputBox(200,200,100,32,"100")
    input_failure_rate = InputBox(200,250,100,32,"0.2")
    input_candidate = InputBox(200,300,100,32,"10")
    labels = [label_sizex,label_sizey,label_trial,label_failure_rate,label_dumac]
    input_boxes = [input_sizex,input_sizey,input_trial,input_failure_rate,input_candidate]

    flag=True

    while flag:
        mouse = pygame.mouse.get_pos()
        screen.fill((255, 255, 255))
        start_button.draw(screen, mouse)

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
                if start_button.x + start_button.w > mouse[0] > start_button.x \
                        and start_button.y + start_button.h > mouse[1] > start_button.y:
                    txt_box_data=[]
                    for input_box in input_boxes:
                        txt_box_data.append(input_box.text)#get data from input boxes

                    flag=False
                    run1=Sim_board(int(txt_box_data[0]),int(txt_box_data[1]),
                                            int(txt_box_data[2]),float(txt_box_data[3]),int(txt_box_data[4]))#pass data to the simulation board
                    run1.rungame()




        pygame.display.flip()
        clock.tick(30)




