#Source: https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key= lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        
        merged.append(prev)

        
        return merged

if __name__ == '__main__':
    solution = Solution()
    inputList = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    result = solution.merge(inputList)