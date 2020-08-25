#!/usr/bin/python3
from random import *
import tkinter as tk
import turtle
import math

def drawCircle(t,x,y):
    """drawCircle function draw the circle of radius 1 in length on location
    (x,y) """
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()

    t.circle(1)

def drawRectangle(t,x,y,l,b):
    """drawRectangle function draw the rectangle of length = l and width = b on
    location (x,y) """
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()

    #drawing four side of the rectangle
    for _ in range(4):
        if _ % 2 == 0 :
            # Forward turtle by l unit
            t.forward(l)
            # Turn turtle by 90 degree
            t.left(90)
        else:
            # Forward turtle by l unit
            t.forward(b)
            # Turn turtle by 90 degree
            t.left(90)

def Intialization(t,length,width,blockRegion,blockSize):
    """Intialization function draw two rectangle and initialize the block for
    RT and ART algorithm"""

    t.speed(10)
    t.pencolor("black") # Red
    t.pensize(4)

    # first rectangle for RT algorithm
    x1 = 0
    y1 = 0
    t.penup()
    t.setx(x1)
    t.sety(y1)
    t.pendown()
    t.write("RT",font=("Arial",22,"normal"))
    drawRectangle(t,x1,y1,length,width)

    #second rectangle for ART algorithm
    x2 = length+80
    y2 = 0
    t.penup()
    t.setx(x2)
    t.sety(y2)
    t.pendown()
    t.write("ART",font=("Arial",22,"normal"))
    drawRectangle(t,x2,y2,length,width)

    point = blockRegion[0]

    #drawing on the RT algorithm Rectangle
    drawRectangle(t,x1+point[0],y1+point[1],blockSize,blockSize)

    #drawing on the ART algorithm Rectangle
    drawRectangle(t,x2+point[0],y2+point[1],blockSize,blockSize)

def calculate_distance(p1,p2):
    """calculate_distance function compute distance between two points"""
    return int(math.sqrt(pow((p1[0]-p2[0]),2) + pow((p1[1]-p2[1]),2)))

def calculate_min_dist(ci, T, s_Dist):
    """calculate_min_dist function takes a points and compute the distance between ART generates set of points and send the minimum distance)"""
    x2 = 0
    for y in T:
        x1 = calculate_distance(y,ci)
        #print('Candidate Point:', ci, ', Existing Point:', y, ', Distance:', x1, ', Current Shortest Distance:', s_Dist)
        if (x1 < s_Dist):
            s_Dist = x1
            x2 = x1
    return x2

def ART(A,length,width):
    """ART function compute the points which is the farthest from all the generated points by computing the distance from all the points in A list"""

    D = 0
    t = 0
    k = []
    origin = (0,0)

    #initialize the s_Dist with diagonal distance (maximum distance) in rectangle
    s_Dist = calculate_distance(origin,(length,width))

    #generating the 3 points and computing the distance from set
    for i in range(3):
        t = (randint(1,length-1),randint(1,width-1))
        k.append(t)

    #print('\nCandidate Data Points', k)
    #print('Existing Data Points', A)

    #computing for each point in k list
    for ci in k:
        #print('\nExecuting Distance Calculation')
        di = calculate_min_dist(ci, A, s_Dist)
        #print("Shortest Distance:", di)
        if (di > D):
            D = di
            t = ci

    #appending the selected point in A list
    A.append(t)
    #print('New Data Point: ', t)

    #returning the newly generated point in ART algorithm
    return t

def RT(R,length,width):
    """RT function generates a random point between x in range(0,length) and y in range(0,width)"""

    #Random Testing
    t = (randint(1,length-1),randint(1,width-1))

    #appending the selected point in R list
    R.append(t)
    #print('New Data Point: ', t)

    #returning the newly generated point in RT algorithm
    return t

def checkSuccess(point,blockRegion):
    """checkSuccess function checks if points lies within the block and return True """
    if point[0] >= blockRegion[0][0] and point[0] <= blockRegion[1][0] and point[1] >= blockRegion[0][1] and point[1] <= blockRegion[1][1] :
        return True

def demo(t,length,width,blockRegion,blockSize):
    """demo function takes run both the algorithms  first time and compute
    each test case and in last computes the success in number of times
    iterations """

    Intialization(t,length,width,blockRegion,blockSize)

    #initializing the list for ART and RT
    A = []
    R = []

    #selecting the random first random point
    point = (randint(1,length-1),randint(1,width-1))
    A.append(point)
    R.append(point)

    #drawing the point the turtle screen
    drawCircle(t,point[0],point[1])
    drawCircle(t,point[0]+length+ 80,point[1])


    #check if first points lies in the region
    if checkSuccess(point,blockRegion) == True:
        print("Test case : {:3d}  RT - Hit!!! ART - Hit!!!" .format(len(A)))
    else:
        print("Test case : {:3d}  RT - missed; ART - missed" .format(len(A)))
        #run RT and ART until one gets success
        while True:

            rtPoint = RT(R,length,width)
            drawCircle(t,rtPoint[0],rtPoint[1])

            artPoint = ART(A,length,width)
            drawCircle(t,artPoint[0]+length+ 80,artPoint[1])

            if checkSuccess(artPoint,blockRegion) == True and checkSuccess(rtPoint,blockRegion) == True:
                print("Test case : {:3d}  RT - Hit!!! ART - Hit!!!" .format(len(A)))
                break
            elif checkSuccess(artPoint,blockRegion) == True:
                print("Test case : {:3d}  RT - missed; ART - Hit!!!" .format(len(A)))
                break
            elif checkSuccess(rtPoint,blockRegion) == True:
                print("Test case : {:3d}  RT - Hit!!! ART - missed" .format(len(A)))
                break
            else:
                print("Test case : {:3d}  RT - missed; ART - missed" .format(len(A)))


    while True:
        number = input("How many more competitions do you want to run ? ")
        try:
            number = int(number)
            break
        except:
            print("Please enter a integer value. ")

    artWinCount = 0;
    rtWinCount = 0

    for i in range(number):
        t.reset()
        Intialization(t,length,width,blockRegion,blockSize)

        #initializing the list for ART and RT
        A = []
        R = []

        #selecting the random first random point
        point = (randint(1,length-1),randint(1,width-1))
        A.append(point)
        R.append(point)

        #drawing the point the turtle screen
        drawCircle(t,point[0],point[1])
        drawCircle(t,point[0]+length+ 80,point[1])

        print("Iteration  : {:2d}" .format(i))
        #check if first points lies in the region
        if checkSuccess(point,blockRegion) == True:
            print("\tTest case : {:3d}  RT - Hit!!! ART - Hit!!!" .format(len(A)))
        else:
            print("\tTest case : {:3d}  RT - missed; ART - missed" .format(len(A)))
            #run RT and ART until one gets success
            while True:

                rtPoint = RT(R,length,width)
                drawCircle(t,rtPoint[0],rtPoint[1])

                artPoint = ART(A,length,width)
                drawCircle(t,artPoint[0]+length+ 80,artPoint[1])

                if checkSuccess(artPoint,blockRegion) == True and checkSuccess(rtPoint,blockRegion) == True:
                    print("\tTest case : {:3d}  RT - Hit!!! ART - Hit!!!" .format(len(A)))
                    artWinCount += 1
                    rtWinCount += 1
                    break
                elif checkSuccess(artPoint,blockRegion) == True:
                    print("\tTest case : {:3d}  RT - missed; ART - Hit!!!" .format(len(A)))
                    artWinCount += 1
                    break
                elif checkSuccess(rtPoint,blockRegion) == True:
                    print("\tTest case : {:3d}  RT - Hit!!! ART - missed" .format(len(A)))
                    rtWinCount += 1
                    break
                else:
                    print("\tTest case : {:3d}  RT - missed; ART - missed" .format(len(A)))

    print("\n\n{} competitions have been completed, of which RT wins {} times and ART wins {} times" .format(number,rtWinCount,artWinCount))

if __name__ == "__main__":

    """setting up tkinter and turtle screen for drawing and calling demo function """

    #initial Dimension for 2 D plot
    length = 400
    width = 200

    while True:
        failureRate = input("Enter a failure rate : ")
        try:
            failureRate = float(failureRate)
            if failureRate > 0.0 and failureRate < 1.0 :
                break
            else:
                raise ValueError()
        except ValueError:
            print("Please enter a value greater than 0 and less than 1.")

    #generating random location for block of size 50 (square)
    blockSize = int(50*failureRate)
    while True:
        point = (randint(1,length-1),randint(1,width-1))
        if point[0] + blockSize < length  and point[1] +blockSize < width:
            break

    #computing the block region for test cases testing
    blockRegion = [ point, (point[0]+blockSize,point[1]+blockSize)]

    root = tk.Tk()
    canvas = tk.Canvas(master = root, width = 800, height = 600)
    canvas.pack(side=tk.LEFT)


    screen = turtle.TurtleScreen(canvas)
    screen.setworldcoordinates(-100, 400,980,-100)

    t = turtle.RawTurtle(screen,visible=True)
    t.speed(10)
    t.pencolor("black") # Red
    t.pensize(4)


    #calling demo function
    demo(t,length,width,blockRegion,blockSize)

    root.mainloop()
