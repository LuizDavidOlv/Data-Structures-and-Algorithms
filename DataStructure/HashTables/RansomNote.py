#Source: https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

from typing import Counter

class BetterSolution: # Time complexity: O(n+m)
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        #This line constructs a counter (essentially a hash map) for the characters in the magazine string.
        count = Counter(magazine) # Time complexity: O(m)
       
        for letter in ransomNote: # Time complexity: O(n)
            if letter not in count or count[letter] == 0:
                return False
            else:
                count[letter] -= 1

        return True
    
if __name__ == '__main__':
    ransomNote = "aaaa"
    magazine = "aab"
    print(BetterSolution.canConstruct(ransomNote, magazine)) 
