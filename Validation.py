def validation(V, w):
    result = 0
    for k in range(0, len(V)):
        xi = V[k][0]
        ye = V[k][1]
        yCap = float(w[0] * xi) + float(w[1] * xi)
        tempResult = ye - yCap
        tempResult = tempResult * tempResult
        result += tempResult

    return result