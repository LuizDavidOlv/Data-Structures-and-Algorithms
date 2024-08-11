# Zip_longest vs zip: https://medium.com/@bonifacechigozie/understanding-zip-longest-vs-zip-in-python-real-life-use-cases-c4204e6aa57e

from itertools import zip_longest

class Solution: 
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitedString = s.split()

        patternLength = len(set(pattern))
        stringLength = len(set(splitedString))
        zipedIterablesLength = len(set(zip_longest(pattern,splitedString)))

        return (patternLength == stringLength == zipedIterablesLength)

            

if __name__ == '__main__':
    pattern = "aabbbbacdef"
    s = "dog dog cat cat cat cat dog fish elephant ant tiger" 
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    if result:
        print("Passed")
    else:
        print("Failed")
    
    pattern = "abba"
    s = "dog cat cat fish"
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    if not result:
        print("Passed")
    else:
        print("Failed")
    
    pattern = "aaaa"
    s = "dog cat cat dog"
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    if not result:
        print("Passed")
    else:
        print("Failed")
    
    pattern = "abba"
    s = "dog dog dog dog"
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    if not result:
        print("Passed")
    else:
        print("Failed")
    
    pattern = "abba"
    s = "dog cat cat dog"
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    if result:
        print("Passed")
    else:
        print("Failed")
    
    pattern = "ab"
    s = "dog dog"
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    if not result:
        print("Passed")
    else:
        print("Failed")
    
    pattern = "ab"
    s = "dog cat"
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    if result:
        print("Passed")
    else:
        print("Failed")
    
    pattern = "ab"
    s = "dog cat dog"
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    if not result:
        print("Passed")
    else:
        print("Failed")

    pattern = "abab"
    s = "dog cat cat dog"
    solution = Solution()
    result = solution.wordPattern(pattern, s)
    if not result:
        print("Passed")
    else:
        print("Failed")
        