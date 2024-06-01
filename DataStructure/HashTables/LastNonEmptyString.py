# https://leetcode.com/problems/apply-operations-to-make-string-empty/description/

from typing import Counter

class BetterSolution:
    def lastNonEmptyString(s):
        # Reversed so order of char keys in Counter will be from right to left in s.
        # We want this ordering because chars will be removed from left to right, 
        # so the remaining chars before the last operation will be the right-most ones 
        # (i.e. the first chars we encounter when iterating right to left in s)
        counts = Counter(reversed(s))

        # only the chars with the max count will remain before the last operation
        max_count = max(counts.values())
        response = ""

       # reverse again to get order of chars before last operation from left to right 
        # reversedCounts = reversed(counts)
        # for char in reversedCounts:
        #     if counts[char] == max_count:
        #         response += char

        return "".join(char for char in reversed(counts) if counts[char] == max_count)


if __name__ == '__main__':
   print(BetterSolution.lastNonEmptyString("aabcbbcaad"))