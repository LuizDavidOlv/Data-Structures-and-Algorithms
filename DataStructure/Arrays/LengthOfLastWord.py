#Source: https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while s[end] == " ":
            end -= 1
        
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        
        return end - start


if __name__ == '__main__':
    solution = Solution()
    result = solution.lengthOfLastWord("kjdhf kjhsdf jjjj j j j  world    ")
    if result == 5:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.lengthOfLastWord(" ")
    if result == 0:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.lengthOfLastWord("a ")
    if result == 1:
        print("Test Passed")
    else:
        print("Test Failed")