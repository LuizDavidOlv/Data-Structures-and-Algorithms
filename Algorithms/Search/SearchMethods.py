from BinarySearch.Example import BinarySearch


class SearchMethods:
    def __init__ (self, sortedList: list[int], num: int):
        self.sortedList = sortedList
        self.num = num
    
    def binarySearch(self) -> list[int]:
        return BinarySearch.search(self.sortedList, self.num)
    


if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    sorted_list = [2, 3, 4, 10, 40]
    num = 2
    search_methods = SearchMethods(sorted_list, num)
    result = search_methods.binarySearch()
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
    print('\n')
    