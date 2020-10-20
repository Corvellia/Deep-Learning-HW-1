import random

def Linear_Learner(E, eta, iterations):
    w = []
    w.append(random.randint(0, 50))
    w.append(random.randint(0, 50))

    for z in range(int(iterations)):
        for k in range(0, len(E)):
            xi = E[k][0]
            ye = E[k][1]
            yCap = float(w[0] * 1) + float(w[1] * xi)
            delta = float(ye - yCap)
            #for x in range(0, len(w)):
            w[1] = float(w[1] + eta * delta * xi)
            w[0] = float(w[0] + eta * delta * 1)

    return w