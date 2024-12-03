# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_count = count = 0

        for i in range(k):
            if s[i] in vowels:
                count +=1
        
        max_count = count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count-=1
            
            if s[i] in vowels:
                count += 1
            
            if count > max_count:
                max_count = count
        
        return max_count