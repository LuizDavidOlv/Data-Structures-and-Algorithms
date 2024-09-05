class Solution:
    def calculate(self, s: str) -> int:
        sum = 0
        s1 = s.replace(" ","").replace(")","").replace("(","")
        s_list = list(s1)
        operators = ["+","-"]
        list_len = len(s_list)
        temp_i =0 
        for i in range(list_len):
            i = temp_i
            stringNum = ""
            if list_len == 1:
                return int(s_list[0])
            if i+1 >= list_len:
                break
            if s_list[i] in operators:
                if s_list[i] == "-":
                    stringNum = s_list[i]
                i += 1
                if s_list[i] == "-":
                    stringNum = ""
                    i += 1
            tempStringNum = ""
            while s_list[i] not in operators:
                tempStringNum += s_list[i]
                i += 1
                if i >= list_len:
                    break
            stringNum += tempStringNum
            sum += int(stringNum)
            temp_i = i
        return sum


if __name__ == '__main__':
    solution = Solution()
    result = solution.calculate("1 + 1")
    if result == 2:
        print("Passed")
    else:
        print("Failed")
    result = solution.calculate(" 2-1 + 2 ")
    if result == 3:
        print("Passed")
    else:
        print("Failed")
    result = solution.calculate("(1+(4+5+2)-3)+(6+8)")
    if result == 23:
        print("Passed")
    else:
        print("Failed")
    result = solution.calculate("1")
    if result == 1:
        print("Passed")
    else:
        print("Failed")
    result = solution.calculate("1-(     -2)")
    if result == 3:
        print("Passed")
    else:
        print("Failed")



#Source: https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150

# class temp:
#     def calculate(self, s: str) -> int:
#         stack = []
#         s1 = s.replace(" ","").replace("(","").replace(")","")
#         s_list = list(s)
#         operators = ["+","-"]
#         constrains = ["(",")"]
#         #remove contrains from s_list

#         strings = ["+","-","(",")"]
#         list_len = len(s_list)
#         for i in list_len:
#             if i+2 >= list_len:
#                     break
#             if s_list[i] not in strings and s_list[i+2] not in strings:
#                 sum = 0 
#                 while s_list[i+1] in operators:
#                     if s_list[i+1] == "+":
#                         sum += s_list[i+2]
#                     if s_list[i+1] == "-"
#                         sum -= s_list[i+2]
#                     i += 1
#                 stack.append(sum)
#             else:
#                 stack.append(s_list[i])
#                 i += 1

