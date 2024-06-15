from typing import Counter

class Solution:
    def isIsomorphic(s: str, t: str) -> bool:
        indexS = [0] * 200 # Stores index of characters in string s
        indexT = [0] * 200 # Stores index of characters in string t
        
        length = len(s) # Get the length of both strings
        
        if length != len(t): # If the lengths of the two strings are different, they can't be isomorphic
            return False
        
        for i in range(length): # Iterate through each character of the strings
            if indexS[ord(s[i])] != indexT[ord(t[i])]: # Check if the index of the current character in string s is different from the index of the corresponding character in string t
                return False # If different, strings are not isomorphic
            
            indexS[ord(s[i])] = i + 1 # updating position of current character
            indexT[ord(t[i])] = i + 1
        
        return True # If the loop completes without returning false, strings are isomorphic

    



if __name__ == '__main__':
    s = "egg"
    t = "aad"
    result1 = Solution.isIsomorphic(s, t) 
    if result1 == True:
        print("Test passed")
    else:
        print("Test failed")
        exit()
    s = "foo"
    t = "bar"
    result2 = Solution.isIsomorphic(s, t)
    if result2 == False:
        print("Test passed")
    else:
        print("Test failed")
        exit()
    s = "paper"
    t = "title"
    result3 = Solution.isIsomorphic(s, t)
    if result3 == True:
        print("Test passed")
    else:
        print("Test failed")
        exit()
    s = "badc"
    t = "baba"
    result4 = Solution.isIsomorphic(s, t)
    if result4 == False:
        print("Test passed")
    else:
        print("Test failed")
        exit()
    s = "bbbaaaba"
    t = "aaabbbba"
    result5 = Solution.isIsomorphic(s, t)
    if result5 == False:
        print("Test passed")
    else:
        print("Test failed")
        exit()
   