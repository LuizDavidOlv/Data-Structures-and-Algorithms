#Source: https://leetcode.com/problems/longest-common-prefix/submissions/1378129181/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        return base
  
  
if __name__ == '__main__':
    solution = Solution()
    result = solution.longestCommonPrefix(["flower","flow","flight"])
    if result == "fl":
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.longestCommonPrefix(["dog","racecar","car"])
    if result == "":
        print("Test Passed")
    else:
        print("Test Failed")
    
