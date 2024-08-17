class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if (num-1) not in num_set:
                length = 1
                while(num+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest


if __name__ == '__main__':
    solution = Solution()

    result = solution.longestConsecutive([1,2,0,1])
    if result == 3:
        print("Passed")
    else:
        print("Failed")

    result = solution.longestConsecutive([100, 4, 200, 1, 3, 2])
    if result == 4:
        print("Passed")
    else:
        print("Failed")

    result = solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
    if result == 9:
        print("Passed")
    else:
        print("Failed")

    result = solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1,9])
    if result == 10:
        print("Passed")
    else:
        print("Failed")
