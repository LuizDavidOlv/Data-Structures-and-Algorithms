class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                elif token == "/":
                    result = int(first / second)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == '__main__':
    solution = Solution()
    result = solution.evalRPN(["2", "1", "+", "3", "*"])
    if result == 9:
        print("Passed")
    else:
        print("Failed")
    result = solution.evalRPN(["4", "13", "5", "/", "+"])
    if result == 6:
        print("Passed")
    else:
        print("Failed")
    result = solution.evalRPN(["10", "6", "9", "3", "/", "-11", "*", "/", "*", "17", "+", "5", "+"])
    if result == 22:
        print("Passed")
    else:
        print("Failed")
    result = solution.evalRPN(["18"])
    if result == 18:
        print("Passed")
    else:
        print("Failed")
    result = solution.evalRPN(["4", "3", "-"])
    if result == 1:
        print("Passed")
    else:
        print("Failed")
    result = solution.evalRPN(["4", "3", "+"])
    if result == 7:
        print("Passed")
    else:
        print("Failed")
    result = solution.evalRPN(["4", "3", "*"])
    if result == 12:
        print("Passed")
    else:
        print("Failed")
    result = solution.evalRPN(["4", "3", "/"])
    if result == 1:
        print("Passed")
    else:
        print("Failed")