from random import *

f = 5

def calculate_min_dist(ci, T):
    x2 = 0
    s_Dist = 100
    for y in T:
        x1 = abs(y - ci)
        print('Candidate Value:', ci, ', Existing Value:', y, ', Difference:', x1, ', Current Shortest Distance:', s_Dist)
        if (x1 < s_Dist):
            s_Dist = x1
            x2 = x1
    return x2

def ART(T):
    D = 0
    t = 0
    k = [randint(1, 100), randint(1, 100), randint(1, 100)]
    print('\nCandidate Data Points', k)
    print('Existing Data Points', T)
    for ci in k:
        if(len(T) < 1):
            if(ci > D):
                D = ci
                t = ci
        else:
            print('\nExecuting Distance Calculation')
            di = calculate_min_dist(ci, T)
            print("Shortest Distance:", di)
            if (di > D):
                D = di
                t = ci
    T.append(t)
    print('New Data Point: ', t)
    return T

def main():
    T = []
    while True:
        data = ART(T)
        if(data[-1] < f):
            print("\nIteration(s):", len(data))
            print("\nFinal Data Points:", data)
            break
main()