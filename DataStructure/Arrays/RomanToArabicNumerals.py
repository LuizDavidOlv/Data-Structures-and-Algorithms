class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumeral = s.replace("CM", "A").replace("CD", "B").replace("XC", "Y").replace("XL", "Z").replace("IX", "W").replace("IV", "IIII")

        result = 0
        toIntDict =[
        ('M', 1000),
        ('A', 900),
        ('D', 500),
        ('B', 400),
        ('C', 100),
        ('Y', 90),
        ('L', 50),
        ('Z', 40),
        ('X', 10),
        ('W', 9),
        ('V', 5),
        ('I', 1),
        ]

        for key,value in toIntDict:
            while key in romanNumeral:
                result += value
                romanNumeral = romanNumeral.removeprefix(key)
        
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.romanToInt("MCMXCIV")
    if result == 1994:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.romanToInt("IV")
    if result == 4:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.romanToInt("IX")
    if result == 9:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.romanToInt("LVIII")
    if result == 58:
        print("Test Passed")
    else:
        print("Test Failed")
    
    result = solution.romanToInt("MCMXCIV")
    if result == 1994:
        print("Test Passed")
    else:
        print("Test Failed")