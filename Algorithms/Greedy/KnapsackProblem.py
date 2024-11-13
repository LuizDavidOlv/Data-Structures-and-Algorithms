'''
# Source: https://www.geeksforgeeks.org/fractional-knapsack-problem/

#* Given the weights and profits of N items, in the form of {profit, weight} put these items in a knapsack of capacity W to get the maximum total profit in the knapsack. 
#* In Fractional Knapsack, we can break items for maximizing the total value of the knapsack.


#* Input: arr[] = {{60, 10}, {100, 20}, {120, 30}}, W = 50
#* Output: 240 
#* Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. 
#*Hence total price will be 60+100+(2/3)(120) = 240


#* Input:  arr[] = {{500, 30}}, W = 10
#* Output: 166.667

'''

from typing import List


class Solution:
    def fractionalKnapsack(self, pAw: List[List[int]], cap: int):

        #Sorting Item on basis of ratio. This way, the most valuable (per unit weight) items are considered first.
        pAw.sort(key=lambda x: (x[0]/x[1]), reverse = True)

        maximumProfit = 0
        
        for item in pAw:
            if cap >= item[1]:
                cap -= item[1]
                maximumProfit += item[0]
            else:
                weightedProfit = item[0]*(cap/item[1])
                maximumProfit += weightedProfit
                break



        return maximumProfit


if __name__ == '__main__':
    solution = Solution()
    profits_and_weights = [[100, 20], [60, 10],  [120, 30]]
    capacity = 50
    result = solution.fractionalKnapsack(profits_and_weights, capacity)
    print(result)