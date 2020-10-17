import math
import random
import sys
from File_Loader import *
'''print("Hello HW1!")

print(math.exp(1))

test = float(.01)

print(test)

testing = input()
testing = testing.split()
wahoo = []
wahoo.append(testing)

print(testing)

for line in sys.stdin:
    print(line.split())
'''
eta = .00000001
iterations = 10000

def pretty_print(w, eta, iterations):
    print("CS-5001: HW#1")
    print("Programmer: Albert J Berger")
    print("\nTraining:\nUsing Learning Rate = " + str(eta))
    print("Using " + str(iterations) + " iterations")
    print("\nOutput:\nw0 = " + str(w[0]) + "\nw1 = " + str(w[1]))
    print("\nValidation\nSum-of-Squares Error = n/a")



def Linear_Learner(E, eta, iterations):
    w = []
    w.append(random.randint(0, 50))
    w.append(random.randint(0, 50))

    #print("Initializing w!!")
    #print(w)
    for z in range(int(iterations)):
        for k in range(0, len(E)):
            xi = E[k][0]
            #print("xi: " + str(xi))
            ye = E[k][1]
            #print("ye: " + str(ye))
            yCap = float(w[0] * xi) + float(w[1] * xi)
            #print("ycap: " + str(yCap))
            delta = ye - yCap
            #print("delta: " + str(delta))
            for x in range(0, len(w)):
                w[x] = float(w[x] + eta * delta * xi)
                #print("New w: ")
                #print(w)
            
    return w



E = file_loader("chocodata.txt")
w = Linear_Learner(E, eta, iterations)
pretty_print(w, eta, iterations)