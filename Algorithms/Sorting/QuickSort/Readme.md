# Time Complexity: Ω(n log(n)) — O(n²)

# Explanation:
    Quick sort is also one of the fastest algorithms. To perform it, pick one element in the data-set and use it as something called a pivot. A pivot is an element 
that is used to compare other elements in the data-set and determine in what position they should be. The first pivot can be a random element in the data-set but by
convention, the first or last element is used. The first objective will be getting the frist pivot to its correct position in the data-set, to achieve this, we have
to sort the elements such that all the elements that are bigger than the pivot are sent to the right of the pivot and all the elements that are smaller than the pivot
are sent to the left of the pivot.