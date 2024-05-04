# https://leetcode.com/problems/apply-operations-to-make-string-empty/description/

def lastNonEmptyString(s):
    while s != "":
        ocurrence = []
        temp = ""
        for char in s:
            if(char not in ocurrence):
                temp+=char
                ocurrence.append(char)
                s = s.replace(char, "",1)
            if(s == ""):
                return temp

print(lastNonEmptyString("aabcbbca"))