# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def compress(self, chars: List[str]) -> int:
        initialSize = len(chars)
        chars.append(None)
        s = []
        s.append(chars[0])
        rep = 1
        for i in range(1, initialSize):
            if i < initialSize and chars[i] == chars[i-1]:
                rep += 1   
                if chars[i] != chars[i+1] and rep > 0:
                    repList = list(str(rep))
                    for num in repList:
                        s.append(num)
                    rep = 1       
            else:
                s.append(chars[i])
        chars.pop()
        chars[0:0] = s
        return len(chars)-initialSize
