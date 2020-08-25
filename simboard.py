import pygame
import random
import math
import Class
import sys
import start

pygame.init()
pygame.font.init()
COLOR_INACTIVE = (125,125,125)
COLOR_ACTIVE = (0, 0, 0)
LIGHT_GREEN= (0,255,0)
GREEN = (0,200,0)
My_font = pygame.font.SysFont("Comic Sans MS", 20)


class Sim_board():
    def __init__(self, sizex, sizey, number_of_trial, failurerate, number_of_candidate):
        """Class variable for the GUI"""
        self.failure_rate = failurerate
        self.height = sizex * 2
        self.width = sizey * 2
        self.caption = "Task 1"
        self.background_colour = (255, 255, 255)
        self.screen_size = [self.width / 2, self.height / 2]
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.canvas = pygame.Surface((self.width, self.height))
        self.number_of_trial = number_of_trial
        self.number_of_candidate = number_of_candidate
        self.speed=60
        """class variable for algorithm"""

    def rungame(self):
        """Initializing test Canvas' object includes the separator Lines"""
        pygame.display.set_caption(self.caption)
        self.canvas.fill(self.background_colour)
        self.p1_camera = pygame.Rect(0, 0, self.width / 2, self.height / 2)
        self.p2_camera = pygame.Rect(self.width / 2, 0, self.width / 2, self.height / 2)
        p3_camera = pygame.Rect(0, self.height / 2, self.width / 2, self.height / 2)
        p4_camera = pygame.Rect(self.width / 2, self.height / 2, self.width / 2, self.height / 2)
        self.p5_camera = pygame.Rect(0, self.height / 2 + 40, self.width, self.height / 2 - 40)
        self.sub1 = self.canvas.subsurface(self.p1_camera)
        self.sub2 = self.canvas.subsurface(self.p2_camera)
        sub3 = self.canvas.subsurface(p3_camera)
        sub4 = self.canvas.subsurface(p4_camera)
        self.sub5 = self.canvas.subsurface(self.p5_camera)
        pygame.draw.line(self.sub2, (0, 0, 0), (0, 0), (0, self.height / 2), 10)
        pygame.draw.line(sub3, (0, 0, 0), (0, 0), (self.width / 2, 0), 10)
        pygame.draw.line(sub4, (0, 0, 0), (0, 0), (self.width / 2, 0), 10)
        self.screen.blit(self.sub1, (0, 0))
        self.screen.blit(self.sub2, (self.width / 2, 0))
        self.screen.blit(sub3, (0, self.height / 2))
        self.screen.blit(sub4, (self.width / 2, self.height / 2))
        self.screen.blit(self.sub5, (0, self.height / 2 + 40))
        fpsClock = pygame.time.Clock()

        """create buttons"""
        retry_button = Class.Button(LIGHT_GREEN, GREEN, (3.5/8)*self.width, (6/8*self.height), 80, 40, "Retry")
        add_speed_button = Class.Button((0, 0, 255), (0, 0, 200),(6/8)*self.width,(5.5/8*self.height),40,40,"+")
        reduce_speed_button = Class.Button((0, 0, 255), (0, 0, 200), (6 / 8) * self.width, (6.5/8 * self.height), 40, 40,"-")
        """initializing required variables for ART and RT"""
        # Pygame font initialization
        pygame.font.init()
        My_font = pygame.font.SysFont("Comic Sans MS", 20)

        # user input variables
        trial_amount = self.number_of_trial
        failure_percentage = self.failure_rate

        # General variables
        current_trial = 0
        art_score = 0
        rt_score = 0
        tie_score = 0
        main_flag = True
        steps = 0
        failure_size = self.get_failure_size()
        first_point = self.generate_coordinate(self.screen_size[0], self.screen_size[1])
        failure_coor = self.generate_coordinate(self.screen_size[0] - failure_size, self.screen_size[1] - failure_size)


        # generate first point
        first_point = self.generate_coordinate(self.screen_size[0], self.screen_size[1])

        ## initializing RT variables

        RT_point = first_point
        RT_flag = True
        RT_steps = 0
        RT_fill_flag = False
        RT_is_hit = False

        ## initializing ART variables
        ART_point = first_point
        ART_flag = True
        ART_steps = 0
        prev_points = []
        ART_is_hit = False
        ART_fill_flag = False

        """Main loop of the panel"""
        while main_flag:
            fpsClock.tick(self.speed)
            #print(self.speed)

            Trial_count = My_font.render("Trial Count:" + str(current_trial), False, (0, 0, 0))
            RT_score_count = My_font.render("RT_score:" + str(rt_score), False, (0, 0, 0))
            ART_score_count = My_font.render("ART_score:" + str(art_score), False, (0, 0, 0))
            tie_score_count = My_font.render("Tie_score:" + str(tie_score), False, (0, 0, 0))

            self.screen.blit(self.sub5, (0, self.height / 2 + 20))
            self.screen.blit(Trial_count, (50, int(self.height / 2 + 100)))
            self.screen.blit(RT_score_count, (int(self.width / 4 - self.width / 10), int(self.height / 2 + 30)))
            self.screen.blit(ART_score_count, (int(self.width * 3 / 4 - self.width / 10), int(self.height / 2 + 30)))
            self.screen.blit(tie_score_count, (int(self.width / 2 - self.width / 10), int(self.height / 2 + 80)))
            self.sub5.fill((255, 255, 255))

            """generate failure area"""
            RT_failure_rect = pygame.draw.rect(self.sub1, [255, 0, 0],
                                               [failure_coor[0], failure_coor[1], failure_size, failure_size], 0)
            ART_failure_rect = pygame.draw.rect(self.sub2, [255, 0, 0],
                                                [failure_coor[0], failure_coor[1], failure_size, failure_size], 0)

            mouse = pygame.mouse.get_pos()#get mouse position

            retry_button.draw(self.screen,mouse)
            add_speed_button.draw(self.screen,mouse)
            reduce_speed_button.draw(self.screen,mouse)


            if current_trial < trial_amount:


                """ALGORITHM START HERE IF rt_flag and ART_FLAG represent WHILE"""
                if RT_flag or ART_flag:
                    steps+=1
                    candidates = []
                    for i in range(0, self.number_of_candidate):
                        candidates.append(self.generate_coordinate(self.screen_size[0], self.screen_size[1]))
                    """RT ALGORITHM START HERE"""
                    if (RT_flag):

                        RT_rect = pygame.draw.rect(self.sub1, [100, 255, 100], [RT_point[0], RT_point[1], 5, 5], 0)
                        self.screen.blit(self.sub1, (0, 0))
                        pygame.display.update()

                        # end condition for RT
                        # if (RT_point == failure_coor):  # is in region
                        #     RT_flag = False
                        #     RT_steps = steps

                        if RT_rect.colliderect(RT_failure_rect):
                            RT_flag = False
                            RT_steps = steps
                            # self.sub1.fill(self.background_colour)
                            RT_fill_flag = True
                            self.screen.blit(self.sub1, (0, 0))
                            RT_msg = " RT - HIT"
                        else:
                            # generate next point
                            RT_point = candidates[0]
                            RT_msg = " RT - Missed"
                    """Art Algorithm start here"""
                    if (ART_flag):

                        ART_rect = pygame.draw.rect(self.sub2, [0, 0, 255], [ART_point[0], ART_point[1], 5, 5], 0)
                        self.screen.blit(self.sub2, (self.width / 2, 0))
                        pygame.display.update()

                        # end condition for ART
                        # if (ART_point == failure_coor):  # is in region
                        #     ART_flag = False
                        #     ART_steps = steps

                        if ART_rect.colliderect(ART_failure_rect):
                            ART_flag = False
                            ART_steps = steps
                            # self.sub2.fill(self.background_colour)
                            ART_fill_flag = True
                            pygame.draw.line(self.sub2, (0, 0, 0), (0, 0), (0, self.height / 2), 10)
                            self.screen.blit(self.sub2, (self.width / 2, 0))
                            ART_msg = " ART - HIT"
                        else:
                            # find new candidate by generating 3 candidates
                            prev_points.append(ART_point)
                            ART_msg = " ART - Missed"

                            # initialize variables
                            potential_candidate = []
                            # print(candidates)

                            max_dist = -math.inf

                            # loop through candidates to find ideal candidate
                            for i in candidates:
                                min_dist = math.inf
                                # loop through previous points and compare distance
                                for j in prev_points:

                                    dist = self.euclidean_distance(i, j)
                                    # print("candidate: " + str(i))
                                    # print("dist: " + str(dist))

                                    # compare distance between candidate and previous points
                                    if dist < min_dist:
                                        min_dist = dist
                                    # print("min dist: " + str(min_dist))

                                # compare distance between candidate
                                if min_dist > max_dist:
                                    potential_candidate = i
                                    max_dist = min_dist
                                # print("max dist: " + str(max_dist))

                            ART_point = potential_candidate
                            # print(potential_candidate)


                            # loop through candidates to find ideal candidate
                            for i in candidates:
                                min_dist = math.inf
                                # loop through previous points and compare distance
                                for j in prev_points:

                                    dist = self.euclidean_distance(i, j)
                                    #print("candidate: " + str(i))
                                    #print("dist: " + str(dist))

                                    # compare distance between candidate and previous points
                                    if dist < min_dist:
                                        min_dist = dist
                                    #print("min dist: " + str(min_dist))

                                # compare distance between candidate
                                if min_dist > max_dist:
                                    potential_candidate = i
                                    max_dist = min_dist
                                #print("max dist: " + str(max_dist))


                            ART_point = potential_candidate
                            #print(potential_candidate)

                    print("Iteration: " + str(current_trial) + "\tTest Case: " + str(steps) + "\t" + RT_msg + "\t" +ART_msg)
                if ART_fill_flag or RT_fill_flag:#Check if Status is completed
                    current_trial += 1
                    """generate new points"""
                    first_point = self.generate_coordinate(self.screen_size[0], self.screen_size[1])
                    failure_coor = self.generate_coordinate(self.screen_size[0] - failure_size,
                                                            self.screen_size[1] - failure_size)
                    ART_point = first_point
                    RT_point = first_point
                    steps=0

                    """condition for score counter"""
                    if ART_fill_flag and RT_fill_flag:
                        tie_score += 1
                    elif ART_fill_flag:
                        art_score += 1
                    elif RT_fill_flag:
                        rt_score += 1

                    """Reset flag"""
                    ART_fill_flag = False
                    RT_fill_flag = False
                    RT_flag = True
                    ART_flag = True



                    self.sub1.fill(self.background_colour)
                    self.sub2.fill(self.background_colour)
                    pygame.draw.line(self.sub2, (0, 0, 0), (0, 0), (0, self.height / 2), 10)


            pygame.display.flip()

            """Event handler of the main panel"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  # check if mouse button is clicked
                    if retry_button.x + retry_button.w > mouse[0] > retry_button.x \
                            and retry_button.y + retry_button.h > mouse[1] > retry_button.y:
                        start.run()
                    if add_speed_button.x + add_speed_button.w > mouse[0] > add_speed_button.x \
                            and add_speed_button.y + add_speed_button.h > mouse[1] > add_speed_button.y:
                        self.speed+=1
                        if self.speed>100:
                            self.speed=2000
                    if reduce_speed_button.x + reduce_speed_button.w > mouse[0] > reduce_speed_button.x \
                            and reduce_speed_button.y + reduce_speed_button.h > mouse[1] > reduce_speed_button.y:
                        self.speed-=1
                        if self.speed <=2:
                            self.speed=2
                        if self.speed >=2000:
                            self.speed=100



    def euclidean_distance(self, coor1, coor2):
        return math.sqrt((coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2)

    def generate_coordinate(self, xlim, ylim):
        return [random.randint(0, xlim), random.randint(0, ylim)]

    def get_failure_size(self):
        total_screen_size = self.screen_size[0] * self.screen_size[1]
        total_failure_size = total_screen_size * self.failure_rate
        failure_size = round(math.sqrt(total_failure_size))
        print("failure_size: ", failure_size)
        return failure_size

