# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        s_list = list(s)
        n = len(s_list)
        max_len = 0

        for i in range(n):
            if s_list[i] in substring:
                index = substring.index(s_list[i])
                substring = substring[index+1:]

            substring.append(s_list[i])

            if len(substring) > max_len:
                max_len = len(substring)

        return max_len      
