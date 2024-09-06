#source: https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def reverseWords(self, s: str) -> str:
        reversedString = ''
        s = s.strip()
        sLength = len(s)
        i = 0
        while i < sLength:
            currentWord= ''
            while i < sLength and s[i] != ' ':
                currentWord += s[i]
                i += 1
            i += 1
            if currentWord != '':
                currentWord  = currentWord if reversedString == '' else  currentWord + ' '
                reversedString = currentWord + reversedString
        
        return reversedString

class Solution2:
    def reverseWords(self, s):
        # Split the string into words
        words = s.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words with spaces
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string
    

if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    s = "the sky is blue"
    solution = Solution2()
    result = solution.reverseWords(s)
    if result == "blue is sky the":
        print("Reverse Words in a String: Passed")
    else:
        print("Reverse Words in a String: Failed")
    
    s = "example   good a"
    result = solution.reverseWords(s)
    if result == "a good example":
        print("Reverse Words in a String: Passed")
    else:
        print("Reverse Words in a String: Failed")
