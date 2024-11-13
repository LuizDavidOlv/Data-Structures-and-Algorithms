
#* You are analyzing the market trends of Dell stock. An Dell financial service model returned an array of integers, PnL (Profits and Loss), 
#* for your portfolio representing that in the ith month, you will either gin or lose PnL[i]. All reported PnL values are positive, representing gains.

#* As part of the analysis, you will peform the following operation on the PnL array any number of times:
    #* - Choose any month i (0 <= i < n) and multiply PnL[i] by -1

#* Find the maximum number of months you can affor to face a loss, i.e. have a neative PnL, 
#* such that the cumulative PnL for each of the n months remains strictly positive i.e. remains greater than 0.

#* Note The cumulative PnL for the ith month is defined as the sum of PnL from the starting month up to the ith month. 
#* For example, the cumulative PnL for the PnL = [3,-2,5,-6,1] is [3,1,6,0,1].

from typing import List

class Solution:
    def getMaxNegativePnL(self, PnL: List[int]):
        gain = 0
        possibleNegativePnL = 0
        for i in range(len(PnL)):
            if gain > PnL[i]:
                PnL[i] = PnL[i]*-1
                possibleNegativePnL += 1

            gain += PnL[i]

        return possibleNegativePnL

PnL = [1,1,1,1,1]
solution = Solution()
result = solution.getMaxNegativePnL(PnL)
# result should be 2
print(f"Result: {result}")