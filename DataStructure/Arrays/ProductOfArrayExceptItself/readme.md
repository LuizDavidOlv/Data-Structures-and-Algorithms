##### Source: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

# Key Concepts

##  High level strategy
- It can be solved by using the concept of prefix and sufffix products
    - Prefix Product: The product of all elements before the current index
    - Suffix Product: The product of all elements after the current index

- By computing these two products for each index and multiplying them, the desired result for each position will be aquired.

## Steps

### Initialize answer array
- Original array is ``nums = [1,2,3,4]``
- ``answer[0] = 1`` 

### Calculate prefix products
- For each index ``i`` of ``nums``, store the product of all elements for the left of ``i`` in ``answer``.
- Process:
    - Iterate from ``i = 1`` to ``n - 1``(where n is the length of the original array)
        - ``answer[i] = nums[i-1] * answer[i-1]``
        - This means the prefix product at index ``i`` is the product of the current element's left neighbor and the prefix product calculated for the left neighbor

### Calculate the suffix products and combine
- For each index ``i``, multiply the current ``answer[i]`` with the product of all elements to the right of ``i``
- Process: 
    - Initialize a variable ``R = 1`` to keep tack of the running suffic product. Initially, it is 1 because there are no elements to the right of the last element.
    - Iterate from ``i = n-1`` down to ``0``
        - Multiply the current prefix product in ``answer[i]`` with the current suffic product ``R``:
            - ``answer[i] = answer[i] * R``
        - Update the suffix product ``R`` by multiplying it with the current element in nums:
            - ``R = R * nums[i]``
        - This step ensures that for each index, ``answer[i]`` contains the product of all elments except ``nums[i]``

## Time and Space Complexity
- Time Complexity: O(n)
    - The algorithm involves two passes over the array: one for prefix products and one for suffix

- Space Complexity: O(n)
    - It was used an extra array ``answer`` of size ``n`` to store the results.
    - Additional variables use constant space of O(1)


## Example walkthrough
``nums = [1, 2, 3, 4]``:

### Calculating Prefix Products  
    Initialize answer[0] = 1  

    i = 1: 
        answer[1] = nums[0] * answer[0]
        answer[1] = 1 * 1 = 1 
        answer[1] = 1 

    i = 2: 
        answer[2] = nums[1] * answer[1]
        answer[2] = 2 * 1
        answer[2] = 2  

    i = 3: 
        answer[3] = nums[2] * answer[2]
        answer[3] = 3 * 2
        answer[3] = 6

- Prefix Products: answer = [1, 1, 2, 6]

### Calculating Suffix Products and Final Answer
    Initialize R = 1

    i = 3: 
        answer[3] = answer[3] * R
        answer[3] = 6 * 1
        answer[3] = 6

        R = R * nums[3]
        R = 1 * 4
        R = 4

    i = 2: 
        answer[2] = answer[2] * R
        answer[2] = 2 * 4
        answer[2] = 8
        
        R = R * nums[2]
        R = 4 * 3
        R = 12
            

    i = 1: 
        answer[1] = answer[1] * R
        answer[1] = 1 * 12
        answer[1] = 12;
        
        R = R * nums[1]
        R = 12 * 2
        R = 24

    i = 0: 
        answer[0] = answer[0] * R
        answer[0] = 1 * 24
        answer[0] = 24; 
        
        R = R * nums[0]
        R = 24 * 1
        R = 24

- Final Answer: answer = [24, 12, 8, 6]


            
    

    
