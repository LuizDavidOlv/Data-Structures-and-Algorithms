#Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solutions/5670898/easy-python3-solution-beats-98/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        hold = [-1 * prices[i] for i in range(n)]
        sell = [hold[i] + prices[i+1] for i in range(n-1)]
        
        maxProfit = 0
        for j in range(len(sell)):
            if sell[j] > 0:
                maxProfit += sell[j] 
        return maxProfit

if __name__ == '__main__':
    solution = Solution()
    prices = [7,1,5,3,3,10]
    result = solution.maxProfit(prices)

