#https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
#* This algorithm uses the Floyd's Tortoise and Hare cycle detection method.
class Solution:
    def isHappy(self, n: int) -> bool:
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while slow!=fast and fast!=1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))

        return fast==1

    def squared(self, n):
        result = 0
        while n>0:
            last = n%10 # Extract the last digit
            result += last * last
            n = n//10 # Remove the last digit
        return result   


if __name__ == '__main__':
    n = 19
    solution = Solution()
    result = solution.isHappy(n)
    if result == True:
        print("19: Passed")
    else:
        print("19: Failed")
    
    n = 2
    result = solution.isHappy(n)
    if result == False:
        print("2: Passed")
    else:
        print("2: Failed")
    
    n = 7
    result = solution.isHappy(n)
    if result == True:
        print("7: Passed")
    else:
        print("7: Failed")
    
    n = 1111111
    result = solution.isHappy(n)
    if result == True:
        print("1111111: Passed")
    else:
        print("1111111: Failed")

  