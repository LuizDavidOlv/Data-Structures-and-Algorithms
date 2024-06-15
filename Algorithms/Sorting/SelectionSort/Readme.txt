Time complexity: Θ(n^2)

    Selection sort operates in a very simple way; it goes through all the elemets in a data-set
one by one comparing the value of one element to the next cheking to see if the element is smaller,
it then saves the smallest element found in a variable and when the interation is complete, it will
insert that saved element to its respective position in that data-set swapping positions with the value
in that position.

    This alhorithm has an Θ(n^2) because in the worst and best-case-scenario we have to iterate
through all the n elements in the array and repear this process N number of times, even if the 
data-set is already sorted there is no telling if it is until all the interations in the algorithm
are complete