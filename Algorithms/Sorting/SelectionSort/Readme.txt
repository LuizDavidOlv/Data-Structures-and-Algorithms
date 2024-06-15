Time complexity: Θ(N^2)
    - One loop to select an element of Array one by one = O(N)
    - Another loop to compare that elements with every other Array element = O(N)
    - Therefore overall complexity =  O(N) * O(N) = O(N*N) = O(N^2)


Auxiliary Space: O(1)
    The only extra memory used is for temporary variable while swapping two values in Array.The 
selection sort never makes more than O(N) swaps and can be useful when memory weiting is costly.


Explanation:
    Selection sort operates in a very simple way; it goes through all the elemets in a data-set
one by one comparing the value of one element to the next cheking to see if the element is smaller,
it then saves the smallest element found in a variable and when the interation is complete, it will
insert that saved element to its respective position in that data-set swapping positions with the value
in that position.

    This alhorithm has an Θ(n^2) because in the worst and best-case-scenario we have to iterate
through all the n elements in the array and repear this process N number of times, even if the 
data-set is already sorted there is no telling if it is until all the interations in the algorithm
are complete