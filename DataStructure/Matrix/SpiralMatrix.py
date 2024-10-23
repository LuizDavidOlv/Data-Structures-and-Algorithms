from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        result = []
        m, n = len(matrix), len(matrix[0]) #Matrix dimension
        top, bottom = 0, m-1 #Row boundaries
        left, right = 0, n-1 #Column boundaries
        
        while top <= bottom and left <= right:
            #traverse from left to right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1

            #from top to bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            #from right to left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            #from bottom to top
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
                
        return result