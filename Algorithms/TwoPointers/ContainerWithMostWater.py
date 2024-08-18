class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left, right = 0,len(height)-1
        while left < right:
            l_height = height[left]
            r_height = height[right]
            min_height = min(l_height,r_height)
            
            area = (right-left) * min_height
            if area > max_area:
                max_area = area
            
            if r_height < l_height:
                right -= 1
            else:
                left += 1
        
        return max_area


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxArea([1,8,6,2,5,4,8,3,7])
    if result == 49:
        print("Passed")
    else:
        print("Failed")
    result = solution.maxArea([1,1])
    if result == 1:
        print("Passed")
    else:
        print("Failed")
    result = solution.maxArea([4,3,2,1,4])
    if result == 16:
        print("Passed")
    else:
        print("Failed")
    result = solution.maxArea([1,2,1])
    if result == 2:
        print("Passed")
    else:
        print("Failed")
    result = solution.maxArea([1,2,4,3])
    if result == 4:
        print("Passed")
    else:
        print("Failed")
    result = solution.maxArea([1,2,4,3,2,1])
    if result == 6:
        print("Passed")
    else:
        print("Failed")