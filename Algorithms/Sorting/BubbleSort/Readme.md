#### Time Complexity: O(n^2) -- Ω(n)
#### Auxiliray Space: O(1)

# Explanation
- In bubbble sort, within each interation the algorithm will find the highest value and put it 
at the end of the data-set or were that value belongs by comparing each pair of elements in the 
data-set. So Selection Sort sorts from the smallest element to the highest and Bubble Sort from 
highest to lowest. Bubble sort also sorts the lowest elements to be closer to the left because
within each iteration the higher value will swap places with the lower values, so it moves lower
elements to the left and higher elements to the right. 

- The worst-case scenario for this algorithm would be if all the elements in the data-set were in
reverse order making the algorithm make more "swaps", but we do see that the best-case scenario is
not as bad as Selection Sort bacause unlike Selection Sort this algorithm is smart enough to realize
in its first interation that the data-set is already sorted.