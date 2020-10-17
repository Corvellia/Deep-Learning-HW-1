def file_loader(fname):
    E = []
    with open(fname) as f:
        for line in f:
            E.append(line.split())
    
    for x in range(0, len(E)):
        E[x][0] = int(E[x][0])
        E[x][1] = int(E[x][1])
    #print(E)

    return E