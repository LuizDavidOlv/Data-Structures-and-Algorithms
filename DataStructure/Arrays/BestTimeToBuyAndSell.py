#Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minValue = prices[0]
        profit = 0
        for price in prices:
            if price < minValue:
                minValue = price
            tempProfit = price - minValue
            if tempProfit > profit:
                profit = tempProfit
        return profit
    

if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit([7,1,5,3,6,4])
    if result == 5:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.maxProfit([7,6,4,3,1])
    if result == 0:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.maxProfit([1,2])
    if result == 1:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.maxProfit([2,4,1])
    if result == 2:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.maxProfit([3,2,6,5,0,3])
    if result == 4:
        print("Test Passed")
    else:
        print("Test Failed")
