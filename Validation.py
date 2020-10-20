def validation(V, w):
    result = 0
    for k in range(0, len(V)):
        xi = V[k][0]
        ye = V[k][1]
        yCap = float(w[0] * 1) + float(w[1] * xi)
        tempResult = float(ye - yCap)
        tempResult = float(tempResult * tempResult)
        result += tempResult

    return result