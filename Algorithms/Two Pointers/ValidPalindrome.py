# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
class OptimalSolution:
    def isPalindrome(s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))

class Solution:
    def isPalindrome(text: str) -> bool:
        #only keep alphanumeric characters
        text = "".join([c.lower() for c in text if c.isalnum()])
        left = 0
        arrSize = len(text)
        right = arrSize -1
        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    s = "A man, a plan, a canal: Panama"
    if Solution.isPalindrome(s):
        print("Is palindrome.")
    else:
        print("Is not palindrome.")
