import random

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
            delta = float(ye - yCap)
            #print("delta: " + str(delta))
            for x in range(0, len(w)):
                w[x] = float(w[x] + eta * delta * xi)
                #print("New w: ")
                #print(w)
            
    return w