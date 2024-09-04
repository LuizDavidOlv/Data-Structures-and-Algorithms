#Source: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1 

if __name__ == '__main__':
    solution = Solution()
    result = solution.strStr("aaaaa", "bba")
    if result == -1:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.strStr("aaaaa", "bba")
    if result == -1:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.strStr("aaaaa", "a")
    if result == 0:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.strStr("hello", "hello")
    if result == 0:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.strStr("hello", "helloo")
    if result == -1:
        print("Test Passed")
    else:
        print("Test Failed")
    

    
 