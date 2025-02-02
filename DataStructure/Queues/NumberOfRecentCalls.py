from collections import deque


class Solution1:
    def __init__(self):
        self.requests = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.start] < t - 3000:
            self.start += 1

        return len(self.requests) - self.start

class Solution2:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)