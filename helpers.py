# traverse 
def around(pos, arr, distance = 1, diagonal = True):
    for i in range(0-distance, 1+distance):
        for j in range(0-distance, 1+distance):
            if 0 <= pos[0] + i < arr.shape[0] and 0 <= pos[1] + j < arr.shape[1] and (i,j) != (0,0) and (diagonal == True or i != j):
                yield (pos[0] + i, pos[1] + j)