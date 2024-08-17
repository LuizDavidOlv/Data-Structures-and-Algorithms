from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    

if __name__ == '__main__':
    solution = Solution()
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    if ['eat', 'tea', 'ate'] in result and ['tan', 'nat'] in result and ['bat'] in result:
        print("Passed")
    else:
        print("Failed")
    
    result = solution.groupAnagrams([""])
    if result == [[""]]:
        print("Passed")
    else:
        print("Failed")

    result = solution.groupAnagrams(["a"])
    if result == [["a"]]:
        print("Passed")
    else:
        print("Failed")
    
