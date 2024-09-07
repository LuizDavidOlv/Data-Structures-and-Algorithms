#Source: https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150

from collections import deque


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        increase = True
        resultDict = { i: "" for i in range(numRows)}
        numRows -= 1
        stringsList = list(s)
        index = 0
        for char in stringsList:
            if increase and index >= numRows:
                increase = False
            if not increase and index == 0:
                increase = True

            resultDict[index] += char

            if numRows >= 1:
                if increase:
                    index += 1
                else:
                    index -= 1

        result = ""
        for i in resultDict:
            result += resultDict[i]
        return result


if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    result = solution.convert(s, numRows)
    if result == "PAHNAPLSIIGYIR":
        print("ZigZag Conversion: Passed")
    else:
        print("ZigZag Conversion: Failed")
    
    s = "PAYPALISHIRING"
    numRows = 4
    result = solution.convert(s, numRows)
    if result == "PINALSIGYAHRPI":
        print("ZigZag Conversion: Passed")
    else:
        print("ZigZag Conversion: Failed")
    
    s = "A"
    numRows = 1
    result = solution.convert(s, numRows)
    if result == "A":
        print("ZigZag Conversion: Passed")
    else:
        print("ZigZag Conversion: Failed")
    
    s = "AB"
    numRows = 1
    result = solution.convert(s, numRows)
    if result == "AB":
        print("ZigZag Conversion: Passed")
    else:
        print("ZigZag Conversion: Failed")
    
    s = "AB"
    numRows = 2
    result = solution.convert(s, numRows)
    if result == "AB":
        print("ZigZag Conversion: Passed")
    else:
        print("ZigZag Conversion: Failed")
    
    s = "ABC"
    numRows = 2
    result = solution.convert(s, numRows)
    if result == "ACB":
        print("ZigZag Conversion: Passed")
    else:
        print("ZigZag Conversion: Failed")
    
