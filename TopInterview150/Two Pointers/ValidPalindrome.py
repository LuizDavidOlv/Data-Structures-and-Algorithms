s = "A man, a plan, a canal: Panama"

def isPalindrome(self, s: str) -> bool:
    s = [c.lower() for c in s if c.isalnum()]
    return all (s[i] == s[~i] for i in range(len(s)//2))

print(isPalindrome(isPalindrome, s))