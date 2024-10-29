#source: https://leetcode.com/problems/set-matrix-zeroes/submissions/1436736651/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        firstRowHasZeros = False
        firstColumnHasZeros = False

        # checks if first column has zeros
        for i in range(m):
            if matrix[i][0] == 0:
                firstColumnHasZeros = True
                break

        #checks if first row has zeros
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowHasZeros = True
                break
        

        # Mark rows and columns to be zeroed
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # mark row
                    matrix[0][j] = 0  # mark column
        
        # Zero out cells based on the markers in the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                # If the column marker in the first row is zero, set the current cell to zero
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
                # If the row marker in the first column is zero, set the current cell to zero
                if matrix[i][0] == 0:
                    matrix[i][j] = 0 
        
        if firstColumnHasZeros:
            for i in range(m):
                matrix[i][0] = 0
        
        if firstRowHasZeros:
            for j in range(n):
                matrix[0][j] = 0



        

                
                    

        
