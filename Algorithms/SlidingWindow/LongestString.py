# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

class ListSolution:
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

class SetSolution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        left = 0
        max_length = 0
        list_size = len(s)

        for right in range(list_size):
            while s[right] in sub:
                sub.remove(s[left])
                left+=1
                
            
            sub.add(s[right])

            max_length = max( max_length, right-left+1)

        return max_length


if __name__ == '__main__':
    result = SetSolution().lengthOfLongestSubstring('pwwkew')