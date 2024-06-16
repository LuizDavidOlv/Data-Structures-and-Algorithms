# Time complexity: Θ(N log N)
# Space complexity: O(N)

# Explanation:
        Merge Sorte is considered to be one of the fastest sorting algorithms, it is a bit more complex than Selection and Bubble sort
but is it more efficient. The idea of Merge Sort is to divide the data-sets, sort them and join together. The way this algorithm behaves
is by sorting the left side of the data-set first then the right part and them merging them. Merge sort will divide in two the data-set
until all the elements are separated then it will start joining from left to right until there are only two bigger pairs to join. This 
makes it easy to merge because if we have two parts of a data-set that are both sorted we can then compare the first element in one 
data-set with the other and determine which one is smaller, therefore, pushing that smaller element first into a new data-set.
        This algorithm has the same Time Complexity for both worst and best-case scenarios because even if the array is sorted(best-case)
the algorithm will still have to do the full proceadure to determine whether the data-set is sorted or not.