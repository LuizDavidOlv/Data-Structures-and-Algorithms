def hourglassSum(arr):
    columns = len(arr[0])
    rows = len(arr)
    if(rows < 3 or columns < 3):
        return False
    hg11, hg12, hg13, hg14 = 0, 0, 0, 0
    hg21, hg22, hg23, hg24 = 0, 0, 0, 0
    hg31, hg32, hg33, hg34 = 0, 0, 0, 0 
    hg41, hg42, hg43, hg44 = 0, 0, 0, 0

    for line in arr:
        if(arr[0] == line):
            hg11 = line[0] + line[1] + line[2]
            hg12 = line[1] + line[2] + line[3]
            hg13 = line[2] + line[3] + line[4]
            hg14 = line[3] + line[4] + line[5]
        if(arr[1] == line):  
            hg21 = line[0] + line[1] + line[2]
            hg22 = line[1] + line[2] + line[3]
            hg23 = line[2] + line[3] + line[4]
            hg24 = line[3] + line[4] + line[5]
            hg11 += line[1]
            hg12 += line[2]
            hg13 += line[3]
            hg14 += line[4]
        if(arr[2] == line):
            hg31 = line[0] + line[1] + line[2]
            hg32 = line[1] + line[2] + line[3]
            hg33 = line[2] + line[3] + line[4]
            hg34 = line[3] + line[4] + line[5]
            hg21 += line[1]
            hg22 += line[2]
            hg23 += line[3]
            hg24 += line[4]
            hg11 += line[0] + line[1] + line[2]
            hg12 += line[1] + line[2] + line[3]
            hg13 += line[2] + line[3] + line[4]
            hg14 += line[3] + line[4] + line[5]
        if(arr[3] == line):
            hg41 = line[0] + line[1] + line[2]
            hg42 = line[1] + line[2] + line[3]
            hg43 = line[2] + line[3] + line[4]
            hg44 = line[3] + line[4] + line[5]
            hg31 += line[1]
            hg32 += line[2]
            hg33 += line[3]
            hg34 += line[4]
            hg21 += line[0] + line[1] + line[2]
            hg22 += line[1] + line[2] + line[3]
            hg23 += line[2] + line[3] + line[4]
            hg24 += line[3] + line[4] + line[5]
        if(arr[4] == line):
            hg31 += line[0] + line[1] + line[2]
            hg32 += line[1] + line[2] + line[3]
            hg33 += line[2] + line[3] + line[4]
            hg34 += line[3] + line[4] + line[5]
            hg41 += line[1]
            hg42 += line[2]
            hg43 += line[3]
            hg44 += line[4]
        if(arr[5] == line):
            hg41 += line[0] + line[1] + line[2]
            hg42 += line[1] + line[2] + line[3]
            hg43 += line[2] + line[3] + line[4]
            hg44 += line[3] + line[4] + line[5]

    array = [hg11, hg12, hg13, hg14, 
              hg21, hg22, hg23, hg24, 
              hg31, hg32, hg33, hg34, 
              hg41, hg42, hg43, hg44]
    
    result = hg11
    for num in array:
       if(num > result):
           result = num

    return result;   

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

result = hourglassSum(arr2)

if(result == False):
    print("The matrix is too small to calculate the hourglass")
else:
    print(result)


