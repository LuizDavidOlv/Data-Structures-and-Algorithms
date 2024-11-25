'''
Developers at Dell are working on a text generation utility for one of their new products.

Currently, the utility generates only special strings. A string is special if there are no matching adjacent characters. Given a string of length n, generate a special string of length n that is lexicographically greater than S. If multiple such special strings are possible, then return the lexicographically smallest string among them.

Notes:

Special String: A string is special if there are no two adjacent characters that are the same.
Lexicographical Order: This is a generalization of the way words are alphabetically ordered in dictionaries. For example, "abc" is lexicographically smaller than "abd" because 'c' comes before 'd' in the alphabet.
A string is lexicographically smaller than a string b if and only if one of the following holds:

a is a prefix of b, but is not equal to b. For example, "abc" is smaller than "abcd".
In the first position where a and b differ, the character in a comes before the character in b in the alphabet. For example, "abc" is smaller than "abd" because 'c' comes before 'd'.
Important Considerations:

If the character is 'z', it is the last character in the alphabet and cannot be increased further. The string should not wrap around to 'a' after 'z'.
The output string must not have any adjacent characters that are the same.
Example:

Suppose S = "abbd".

Some of the special strings that are lexicographically greater than s are shown:

| a | b | b | d | → | a | b | b | a |
| a | b | b | d | → | a | b | c | a |
| a | b | b | d | → | a | c | b | a |
| a | b | b | d | → | a | c | b | b |

The lexicographically smallest special string that is greater than "abbd" is "abca".

Function Description

Complete the function getSpecialString in the editor below.

getSpecialString has the following parameter:

s: the input string
Returns

string: the lexicographically smallest string that is greater than s. If no such special string exists, return "-1".
Constraints

1 ≤ |s| ≤ 10^6
s consists of lowercase English letters only.
'''
#* Time Complexity: O(n^2)
#* Algorithm type: Greedy
class Solution:
    def getSpecialString(self, s):
        s_list = list(s)
        list_size = len(s_list)

        # Traverse the array from right to left
        for i in range(list_size-1,-1,-1):
            # Try to replace the current num with the next lexicographical character. 
            # Change the letter to ascii format so it's value can be added. Use ord() method to do so
            for next_letter in range(ord(s_list[i])+1, ord('z')+1):
                # Convert from ascii back to string. Use chr() method to do so
                char = chr(next_letter)

                # Check if the new character causes adjacent duplicates
                if(i>0 and char == s_list[i-1]) or (i<list_size-1 and char == s_list[i+1]):
                    continue

                # Replace the current letter with the new subsequent letter
                s_list[i] = char

                # Reconstruct the rest of the array. Starting from the 
                for j in range(i+1,list_size):
                    for candidate in range(ord('a'),ord('z')+1):
                        candidate_char = chr(candidate)
                        if candidate_char != s_list[j-1]:
                            s_list[j] = candidate_char
                            break

                # Check if the string is special
                is_special = True
                for k in range(1,list_size):
                    if s_list[i] == s_list[i-1]:
                        is_special = False
                        break
                if is_special:
                    return ''.join(s_list)
                else:
                    continue
        return -1

if __name__ == '__main__':
    s = "abbc"
    result = Solution().getSpecialString(s)
    print(result)  # Output: "abca"
