from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return list(res)
    
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate elements for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1  # Initialize the left pointer
            right = n - 1  # Initialize the right pointer

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Found a triplet that sums up to zero
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers
                    left += 1
                    right -= 1

                elif total < 0:
                    # Need a larger sum; move the left pointer to the right
                    left += 1
                else:
                    # Need a smaller sum; move the right pointer to the left
                    right -= 1

        return result
    

if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    solution = Solution2()
    nums = [-1,0,1,2,-1,-4]
    result = solution.threeSum(nums)
    if result == [[-1, -1, 2], [-1, 0, 1]]:
        print("Passed")
    else:
        print("Failed")