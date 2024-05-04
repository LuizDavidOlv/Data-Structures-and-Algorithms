# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

def compareTriplets(a, b):
    aSum = 0
    bSum = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            aSum += 1
        elif b[i] > a[i]:
            bSum += 1
    return aSum, bSum


a = [5, 6, 7]
b = [3, 6, 10]

result = compareTriplets(a, b)

print(result)

 