from typing import List


class BinarySearch:
    def search(sorted_list: List[int], num: int):
        low = 0
        high = len(sorted_list) -1
        while low <= high:
            mid = low + (high - low) // 2
            if sorted_list[mid] == num:
                return mid
            elif sorted_list[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        return -1