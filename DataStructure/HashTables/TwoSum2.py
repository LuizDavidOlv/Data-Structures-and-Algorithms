#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

# Two Pointers Solution on TwoPointers folder

#* HashTable Solution
class Solution(object):
    def twoSum(self, numbers, target):
        visited = {}
        n = len(numbers)

        for i in range(n):
            num = numbers[i]
            if target - num in visited:
                indexI, indexJ = visited[target - num][-1] + 1, i + 1
                return [indexI, indexJ]
            if num not in visited:
                visited[num] = [i]
            else:
                visited[num] += [i]

        return []



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