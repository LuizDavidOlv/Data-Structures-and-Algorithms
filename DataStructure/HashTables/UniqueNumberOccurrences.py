from typing import Counter, List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrCount = Counter(arr)
        return len(set(arrCount.values())) == len(arrCount.values())