from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citLength = len(citations)
        hIndex = 0
        remainingIndexes = citLength
        for i in range(citLength): 
            if citations[i] >= remainingIndexes:
                hIndex = remainingIndexes
                break
            remainingIndexes -= 1
          
        return hIndex
            
        
        
if __name__ == '__main__':
    solution = Solution()
    numList = [1,2]
    result = solution.hIndex(numList)
    print(result)

   


 