#Source: https://leetcode.com/problems/insert-interval/submissions/1453889820/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False

        for interval in intervals:
            if interval[1] < newInterval[0]: 
                #current interval ends before newInterval starts; no overlap 
                result.append(interval)
            elif interval[0] > newInterval[1]:
                # current interval starts after newInterval ends; no overlap
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append(interval)
            else:
                # interval and newInterval overlap
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])
        
        if not inserted:
            result.append(newInterval)
        
        return result