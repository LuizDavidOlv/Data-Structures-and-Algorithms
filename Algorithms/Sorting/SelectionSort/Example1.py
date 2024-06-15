class SelectionSort:
    @staticmethod
    def sort(unsortedList: list[int]) -> list[int]:
        for i in range(len(unsortedList)):
            min_idx = i
            for j in range(i+1, len(unsortedList)):
                if unsortedList[min_idx] > unsortedList[j]:
                    min_idx = j
            unsortedList[i], unsortedList[min_idx] = unsortedList[min_idx], unsortedList[i]

        sortedList = unsortedList.copy()
        return sortedList

if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    unsortedList = [64,25,12,22,11]
    sortedList = SelectionSort.sort(unsortedList)
    print("Sorted List")
    print(sortedList)
    print('\n')