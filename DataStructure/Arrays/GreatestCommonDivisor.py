from math import gcd
from typing import Counter


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if the concatenation of the two strings in reverse order is the same
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of the lengths of the two strings
        gcd_length = gcd(len(str1), len(str2))
        
        # The common divisor string would be the prefix of either string up to the GCD length
        return str1[:gcd_length]
    
if __name__ == '__main__':
    solution = Solution()
    str1 = 'ABCABC'
    str2 = 'ABC'
    result = solution.gcdOfStrings(str1,str2)