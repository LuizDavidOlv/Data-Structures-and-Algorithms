# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isSubsequence(self, s:str, t:str) -> bool:
        s_index, t_index = 0, 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)
    

if __name__ == '__main__':
    solution = Solution()

    result = solution.isSubsequence("", "ahbgdc")
    if result == True:
        print("Passed")
    else:
        print("Failed")

    result = solution.isSubsequence("axc", "ahbgdc")
    if result == False:
        print("Passed")
    else:
        print("Failed")

    result = solution.isSubsequence("aaaaaa", "bbaaaa")
    if result == False:
        print("Passed")
    else:
        print("Failed")

    result = solution.isSubsequence("aaaaaa", "aaaaaa")
    if result == True:
        print("Passed")
    else:
        print("Failed")