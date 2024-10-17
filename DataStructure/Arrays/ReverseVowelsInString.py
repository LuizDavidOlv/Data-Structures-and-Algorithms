# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = 'aeiouAEIOU'
        vowelDict = dict()

        for i in range(len(s_list)):
            if s_list[i] in vowels:
                vowelDict[i] = s_list[i]
        
        values = list(vowelDict.values())[::-1]

        reversed_dict = {key: values[i] for i, key in enumerate(vowelDict.keys())}

        for i in reversed_dict.keys():
            s_list[i] = reversed_dict[i]
        
        return "".join(s_list)


if __name__ == '__main__':
    solution = Solution()
    result = solution.reverseVowels("IceCreAm")
    if result == "AceCreIm":
        print('Passed')
    else:
        print('Failed')