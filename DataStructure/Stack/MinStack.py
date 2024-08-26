# https://leetcode.com/problems/min-stack/description/
class MinStack:

    def __init__(self):
        self.Stack = []
        self.OrderedStack = []

    def push(self, val: int) -> None:
        self.Stack.append(val)
        if not self.OrderedStack:
            self.OrderedStack.append(val)
        elif val >= self.OrderedStack[-1]:
            self.OrderedStack.append(val)
        elif val <= self.OrderedStack[0]:
            self.OrderedStack.insert(0, val)
        else:
            self.OrderedStack.insert(1, val)

    def pop(self) -> None:
        self.OrderedStack.remove(self.Stack[-1])
        self.Stack.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.OrderedStack[0]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(2147483646)
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    minStack.push(2147483646)
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    minStack.push(2147483647)
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    result = minStack.top()
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    if result == 2147483647:
        print("Passed")
    else:
        print("Failed")
    minStack.pop()
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    result = minStack.getMin()
    if result == 2147483646:
        print("Passed")
    else:
        print("Failed")
    minStack.pop()
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    result = minStack.getMin()
    if result == 2147483646:
        print("Passed")
    else:
        print("Failed")
    minStack.pop()
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    minStack.push(2147483647)
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    result = minStack.top()
    if result == 2147483647:
        print("Passed")
    else:
        print("Failed")
    result = minStack.getMin()
    if result == 2147483647:
        print("Passed")
    else:
        print("Failed")
    minStack.push(-2147483648)
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    result = minStack.top()
    if result == -2147483648:
        print("Passed")
    else:
        print("Failed")
    result = minStack.getMin()
    if result == -2147483648:
        print("Passed")
    else:
        print("Failed")
    minStack.pop()
    print(minStack.OrderedStack)
    print(minStack.Stack)
    print("-------------------------")
    result = minStack.getMin()
    if result == 2147483647:
        print("Passed")
    else:
        print("Failed")

