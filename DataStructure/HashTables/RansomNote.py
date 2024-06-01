#Source: https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

from typing import Counter


class BadSolution: # Time complexity: O(nm+n^2)
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        magazineArray = list(magazine) # Time complexity: O(m)
        ransomNoteArray = list(ransomNote) # Time complexity: O(n)
        for letter in ransomNote: # Time complexity: O(n)
            if letter in magazineArray: # Time complexity: O(m)
                magazineArray.pop(magazineArray.index(letter)) # Time complexity: O(m)
                ransomNoteArray.pop(ransomNoteArray.index(letter)) # Time complexity: O(n)
            else:
                return False # Time complexity: O(1)
        return True # Time complexity: O(1)
    # Time complexity sum = O(n) × O(2m+n) = O(n⋅(2m+n)) = O(2nm+n 2) = O(nm+n2)

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
