## Definition of H-index
The h-index is defined as the maximum value of h such that the given researcher 
has published at least h papers that have each been cited at least h times.


## Original Array
originalArray = [22,1,11,2,33,21,11,11]

## Sort in ascending order
sortedArray = [1,2,11,11,11,22,33,21]  
hindex = 0   
listLength = 8



## Compare the current value with the number of remaining indexes
x [ i ] > remaining indexes?  

[1, _, _ , _ , _ , _ , _ , _ ]  
    # How many interation until the end of the array? 8 interaction  
    # 1 > 8 ? No. Keep the original value of 1 in the current position  

currentHighestValue = 1   
hindex= 1

## Do the same for the remaning numbers in the sorted array
[1,2, _ , _ , _ , _ , _ , _ ]  
    # 2 > 7 ? No. Keep the original value of 2 in current position  

hindex = 2  
    # hindex can be updated to 2 bacause it known that the following values will be equal or greater than two.  
    # In the current position the max h-index that can still happen is 6.
        That is because that are only 6 interations left

# x [ i ] > remaining indexes
[1,2,11, _ , _ , _ , _ , _ ]  
    #* 11 >= 6? Yes! In this case 6. So 11 turns into 6  

[1,2,6, _ , _ , _ , _ , _ ]  
    #* Right here we already know that the awnswer will be 6. That is because all the
        following integers will be greater or equal to eleven. By applying the same logic, all the other integers will be turned into the number 6. 

hindex = 6

## Final View
SortedList = [1,2,11,11,11,22,33,21]  
TransformedList= [1,2,6,6,6,6,6,6]  
    #* That is to say that are at least 6 citations in 6 different papers, which 
        corresponde to the definition of h-index




## Code path examples
## Example 1

citations = [1,3,1]  
sorted citations = [1,1,3]

len(citations) = 2  
citLength = len(citations)  
remainingIndexes = citLength  

indexes = [0,1,2]  
x[i] >= remainingIndexes  
index 0: x[0] >= 2  -> 1 >= 2 ? No  
index 0: x[1] >= 1  -> 1 >= 1 ? Yes  
return remainingIndexes


## Example 2

citations = [1,3]  
sorted citations = [1,3]

len(citations) = 1  
citLength = len(citations)  
remainingIndexes = citLength

indexes = [0,1]  
index 0: x[0] >= 1  -> 1 >= 1 ? Yes  
return remainingIndexes


## Example 3

citations = [3]  
sorted citations = [3]  

len(citations) = 0  
citLength = len(citations)  
remainingIndexes = citLength

indexes = [0]  
index 0: x[0] >= 0  -> 3 >= 0 ? Yes  
return remainingIndexes
