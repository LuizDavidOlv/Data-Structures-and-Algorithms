# https://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/

def floodFillUtil(screen, x, y, prevC, newC):
    if(prevC == newC):
        return
    if(x < 0 or x >= M or y < 0 or y >= N):
        return
    if(screen[x][y] != prevC):
        return
    
    screen[x][y] = newC
    floodFillUtil(screen, x + 1, y, prevC, newC)
    floodFillUtil(screen, x - 1, y, prevC, newC)
    floodFillUtil(screen, x, y + 1, prevC, newC)
    floodFillUtil(screen, x, y - 1, prevC, newC)

    return None

def floodFill(screen, x, y, newC):
    prevC = screen[x][y]
    floodFillUtil(screen, x, y, prevC, newC)
 
# Driver Code
screen = [[1, 1, 1, 1, 1, 1, 1, 1], 
          [1, 1, 1, 1, 1, 1, 0, 0], 
          [1, 0, 0, 1, 1, 0, 1, 1], 
          [1, 2, 2, 2, 2, 0, 1, 0], 
          [1, 1, 1, 2, 2, 0, 1, 0], 
          [1, 1, 1, 2, 2, 2, 2, 0], 
          [1, 1, 1, 1, 1, 2, 1, 1], 
          [1, 1, 1, 1, 1, 2, 2, 1]]

# Dimensions of paint screen 
M = 8
N = 8

# Coordinates of the starting point
x = 4
y = 4
newCollor = 3
floodFill(screen, x, y, newCollor)
 
print ("Updated screen after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end = ' ')
    print()