#Source: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort the balloons based on their end coordinates
        points.sort(key=lambda x: x[1])

        arrows = 0
        arrow_pos = float('-inf')

        for balloon in points:
            x_start, x_end = balloon
            # If the current balloon starts after the position of the last arrow
            if x_start > arrow_pos:
                arrows += 1
                arrow_pos = x_end  # Shoot a new arrow at the end of the current balloon

        return arrows


if __name__ == '__main__':
    solution = Solution()
    points= [[10,16],[2,8],[1,6],[7,12]]
    result = solution.findMinArrowShots(points)
    print(result)