class BubbleSort:
    def sort(unsortedList: list[int]) -> list[int]:
        listLength = len(unsortedList)
        for i in range(listLength):
            swapped = False
            for j in range(0, listLength-i-1):
                if unsortedList[j] > unsortedList[j+1]:
                    unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
                    swapped = True
            if swapped == False:
                break

        sortedList = unsortedList.copy()
        return sortedList

if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    unsortedList = [64,25,12,22,11]
    sortedList = BubbleSort.sort(unsortedList)
    print("Sorted List")
    print(sortedList)
    print('\n')