#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

#Hash map solution in the HashTables folder


#* Two Pointers Solution
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            two_sum = numbers[left] + numbers[right]

            if two_sum == target:
                return [left + 1, right + 1]
            elif two_sum < target:
                left += 1
            else:
                right -= 1
            
        return [-1, -1]



if __name__ == '__main__':
    solution = Solution()

    result = solution.twoSum([0,0,3,4], 0)
    if result == [1, 2]:
        print("Passed")
    else:
        print("Failed")

    result = solution.twoSum([2,7,11,15], 9)
    if result == [1, 2]:
        print("Passed")
    else:
        print("Failed")

    result = solution.twoSum([2,3,4], 6)
    if result == [1, 3]:
        print("Passed")
    else:
        print("Failed")

    result = solution.twoSum([-1,0], -1)
    if result == [1, 2]:
        print("Passed")
    else:
        print("Failed")

    result = solution.twoSum([3,24,50,79,88,150,345], 200)
    if result == [3, 6]:
        print("Passed")
    else:
        print("Failed")