#Source: https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = curr_tank = starting_station = 0
        for i in range(len(gas)):
            net_gas = gas[i] - cost[i]
            total_tank += net_gas
            curr_tank += net_gas
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0
        return starting_station if total_tank >= 0 else -1
        

if __name__ == '__main__':
    solution = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    result = solution.canCompleteCircuit(gas,cost)
    print(result)