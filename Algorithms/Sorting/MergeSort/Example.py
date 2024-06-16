class MergeSort:
    def sort(unsortedList: list[int]) -> list[int]:
        listSize = len(unsortedList)
        begin = 0
        end = listSize - 1
        MergeSort.mergeSort(unsortedList,begin,end)
        sortedList = unsortedList.copy()
        return sortedList
    
    def mergeSort(unsortedList: list[int], begin: int, end: int):
        if begin >= end:
            return unsortedList
        mid = begin + (end-begin)//2
        MergeSort.mergeSort(unsortedList,begin,mid)
        MergeSort.mergeSort(unsortedList,mid+1,end)
        MergeSort.merge(unsortedList,begin,mid,end)
    
    # Merge two subLists of list[]
    # First subList is list[left...mid]
    # Second subList is list[mid+1...right]
    def merge(array: list[int], left: int, mid: int, right: int):
        subArrayOne = mid -left + 1
        subArrayTwo = right - mid

        # Create temp arrays
        leftArray = [0] * subArrayOne
        rightArray = [0] * subArrayTwo

        # Copy data to temp arrays leftArray[] and rightArray[]
        for i in range(0, subArrayOne):
            leftArray[i] = array[left + i]
        for j in range(0, subArrayTwo):
            rightArray[j] = array[mid+1+j]

        indexOfSubArrayOne = 0
        indexOfSubArrayTwo = 0
        indexOfMergedArray = left

        # Merge the temp arrays back into list[left...right]
        while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
            if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
                array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
                indexOfSubArrayOne += 1
            else:
                array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
                indexOfSubArrayTwo += 1
            indexOfMergedArray += 1
        
        # Copy the remaining elements of left[], if any
        while indexOfSubArrayOne < subArrayOne:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
            indexOfMergedArray += 1

        # Copy the remaining elements of right[], if any
        while indexOfSubArrayTwo < subArrayTwo:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
            indexOfMergedArray += 1

if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    unsortedList = [64,25,12,22,11]
    sortedList = MergeSort.sort(unsortedList)
    print("Sorted List")
    print(sortedList)
    print('\n')