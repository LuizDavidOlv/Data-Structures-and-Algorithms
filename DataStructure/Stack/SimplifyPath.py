# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')
        for dir in directories:
            if dir == '.' or not dir:
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return f"/{'/'.join(stack)}"


if __name__ == '__main__':
    solution = Solution()
    result = solution.simplifyPath("/home/")
    if result == "/home":
        print("Passed")
    else:
        print("Failed")
    result = solution.simplifyPath("/../")
    if result == "/":
        print("Passed")
    else:
        print("Failed")
    result = solution.simplifyPath("/home//foo/")
    if result == "/home/foo":
        print("Passed")
    else:
        print("Failed")
    result = solution.simplifyPath("/a/./b/../../c/")
    if result == "/c":
        print("Passed")
    else:
        print("Failed")
    result = solution.simplifyPath("/a/../../b/../c//.//")
    if result == "/c":
        print("Passed")
    else:
        print("Failed")
    result = solution.simplifyPath("/a//b////c/d//././/..")
    if result == "/a/b/c":
        print("Passed")
    else:
        print