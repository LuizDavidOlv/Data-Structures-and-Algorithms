from typing import List

class Solution:
    def is_power_of_k(self,readings: List[int], k: int):
        """
        Count how many numbers in `readings` are exat iterger power of `k`.
        Time complexity: O(n + log_k(max_readings))
        """
        if not readings:
            return 0
        
        max_reading = max(readings)

        powers = set()
        p = 1  # includes k^0 = 1
        while p <= max_reading:
            powers.add(p)
            p *= k
        
        count = sum(1 for x in readings if x in powers)
        return count


if __name__ == "__main__":
    readings = [10201, 101, 1030301, 101, 101]
    k = 101
    solution = Solution().is_power_of_k(readings, k)
    print(f"The readings that are power of {k} in {readings} adds up to a total ammount of {solution}")




"""
You are monitoring energy usage in a smart grid system and need to identify specific data patterns in the readings.

Given an array of integers readings representing the energy readings over a period and an integer k, 
count the readings that are powers of k. In this context, a power of k refers to numbers that can be 
expressed as k raised to an integer power (e.g., k0, k1, k2, etc.).

Note: You are not expected to provide the most optimal solution, but a solution with time complexity 
not worse than O(readings.length2) will fit within the execution time limit.

Example

For readings = [2, 4, 7, 8, 16, 32, 120] and k = 2, the output should be solution(readings, k) = 5.

Explanation:
The numbers in the readings list that are powers of 2 are 2 (21), 4 (22), 8 (23), 16 (24), and 32 (25). 
There are 5 such numbers.

For readings = [10201, 101, 1030301, 101, 101] and k = 101, the output should be solution(readings, k) = 5.

Explanation:
The numbers in the readings list that are powers of 10123 are 101 (1011), 10201 (1012), and 1030301 (1013). 
There are 5 such numbers.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer readings

An array of integers representing the energy readings over a period.

Guaranteed constraints:
1 ≤ readings.length ≤ 1000,
2 ≤ readings[i] ≤ 109.

[input] integer k

An integer representing the base of the power to check against the readings.

Guaranteed constraints:
2 ≤ k ≤ 109.
"""