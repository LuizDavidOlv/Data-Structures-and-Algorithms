#Source: https://www.geeksforgeeks.org/two-pointers-technique/
from typing import List

def IsPairSum(A: List[int], N: int, X: int) -> bool:
    i = 0
    j = N -1

    while i<j:
        if A[i] + A[j] == X:
            return True
        elif A[i] + A[j] < X:
            i += 1
        else:
            j -= 1
    return False


if __name__ == "__main__":
    arr = [2,3,5,8,9,10,11]
    val = 17
    arrSize = len(arr)
    arr.sort()
    result = IsPairSum(arr, arrSize, val)
    if result:
        print("Array has two elements with sum ", val)
    else:
        print("Array doesn't have two elements with sum ", val)