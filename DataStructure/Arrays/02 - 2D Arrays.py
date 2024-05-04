# https://www.hackerrank.com/challenges/2d-array/problem

def hourglassSum(arr):
    hourglass_sum_list = []
    range_x = len(arr[0])-1
    range_y = len(arr)-2

    if(range_x+1 < 3 or range_y+2 < 3):
        return False

    for x in range(1, range_x):
        for y in range(0, range_y):
            hourglass_sum_list.append(arr[y][x-1] + arr[y][x] + arr[y][x+1] + arr[y+1][x] + arr[y+2][x-1] + arr[y+2][x] + arr[y+2][x+1])
    
    max_hourglass_sum = max(hourglass_sum_list)
    return max_hourglass_sum


print("Calculating the hourglass of the matrix")


arr = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

arr2 = [        
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
]

arr3 = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

arr4 = [
    [1, 1],
    [1, 1],
    [1, 1]
]
   

result = hourglassSum(arr2)

if(result == False):
    print("The matrix is too small to calculate the hourglass")
else:
    print("The maximum hourglass sum is: ", result)


