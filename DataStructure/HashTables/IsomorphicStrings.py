from typing import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize mappings for both directions
        s_to_t_mapping = {}
        t_to_s_mapping = {}
        
        # Iterate over the characters of both strings
        for char_s, char_t in zip(s, t):
            # Check if char_s is already mapped in s_to_t_mapping
            if char_s in s_to_t_mapping:
                if s_to_t_mapping[char_s] != char_t:
                    return False  # Inconsistent mapping
            else:
                s_to_t_mapping[char_s] = char_t  # Add the mapping
            
            # Check if char_t is already mapped in t_to_s_mapping
            if char_t in t_to_s_mapping:
                if t_to_s_mapping[char_t] != char_s:
                    return False  # Inconsistent mapping
            else:
                t_to_s_mapping[char_t] = char_s  # Add the mapping

        # If all mappings are consistent, the strings are isomorphic
        return True



if __name__ == '__main__':
    solution = Solution()
    s = "egg"
    t = "aad"
    result1 = solution.isIsomorphic(s, t) 
    if result1 == False:
        print("Test passed")
    else:
        print("Test failed")
        exit()
    s = "foo"
    t = "bar"
    result2 = solution.isIsomorphic(s, t)
    if result2 == False:
        print("Test passed")
    else:
        print("Test failed")
        exit()
    s = "paper"
    t = "title"
    result3 = solution.isIsomorphic(s, t)
    if result3 == True:
        print("Test passed")
    else:
        print("Test failed")
        exit()
    s = "badc"
    t = "baba"
    result4 = solution.isIsomorphic(s, t)
    if result4 == False:
        print("Test passed")
    else:
        print("Test failed")
        exit()
    s = "bbbaaaba"
    t = "aaabbbba"
    result5 = solution.isIsomorphic(s, t)
    if result5 == False:
        print("Test passed")
    else:
        print("Test failed")
        exit()
   