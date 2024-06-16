class QuickSort:
    def sort(unsortedList: list[int]) -> list[int]:
        listLength = len(unsortedList)
        QuickSort.quicksort(unsortedList, 0, listLength-1)
        sortedList = unsortedList.copy()
        return sortedList
    
    def quicksort(array: list[int], low: int, high: int) -> list[int]:
        if low < high:
            #Find pivot element
            pivot = QuickSort.partition(array, low, high)
            
            # Recursive call on the left of pivot
            QuickSort.quicksort(array, low, pivot-1)
            # Recursive call on the right of pivot
            QuickSort.quicksort(array, pivot+1, high)

    def partition(array: list[int], low: int, high: int) -> int:
        # Choose the righmost element as a pivot
        pivot = array[high]

        # Pointer for greater element
        i = low -1

        # Traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # If element smaller that pivot in found
                # swap it with the grater element pointed by i
                i = i+1
                 
                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # Swap the pivot element with the grater element specified by i
        (array[i+1], array[high]) = (array[high], array[i+1])

        # Return the position from where partition is done
        return i+1



if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    unsortedList = [64,25,12,22,11]
    sortedList = QuickSort.sort(unsortedList)
    print("Sorted List")
    print(sortedList)