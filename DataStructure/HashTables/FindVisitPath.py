class Solution:
    '''
    # enhance method so it handles ciclic input list
        unordered_circular_list = [('T1T','2QK'),('2QK','UT9'),('1SF','2QK'),('2QK','II0'),('UT9','T1T')]
        output should be ordered_list1 == [('1SF','2QK'),('2QK','UT9'),('UT9','T1T'),('T1T','2QK'),('2QK','II0')]:
        unordered_circular_list2 = [('2QK','Y2K'),('2QK','UT9'),('1SF','2QK'),('Y2K','II0'),('UT9','2QK')]
        output should be ordered_list2 == [('1SF','2QK'),('2QK','UT9'),('UT9','2QK'),('2QK','Y2K'),('Y2K','II0')]:

    # enhance method so it handles more than one list as input and output
        many_unordered_lists =  [('T1T','PO9'),('2QK','TX8'),('1SF','2QK'),('Y2K','II0'),('UT9','T1T')]
        
    '''
    def find_visit_path(self, visitList: list)->list:
        ordered_list = []
        lookup = {}
        first_elements = set()
        second_elements = set()

        # Step 1: Build a dictionary for quick lookups
        for first, second in visitList:
            lookup[first] = second
            first_elements.add(first)
            second_elements.add(second)

        # lookup = {first: second for first, second in visitList}
        # first_elements = set(lookup.keys())
        # second_elements = set(lookup.values())

        start_point = first_elements - second_elements

        current = start_point.pop() if start_point else None
        while current in lookup:
            next_point = lookup[current]
            ordered_list.append((current,next_point))
            current = next_point

        return ordered_list


if __name__ == '__main__':
    solution = Solution()

    unordered_list = [('T1T','Y2K'),('2QK','UT9'),('1SF','2QK'),('Y2K','II0'),('UT9','T1T')]
    ordered_list = solution.find_visit_path(unordered_list)
    if ordered_list == [('1SF', '2QK'), ('2QK', 'UT9'), ('UT9', 'T1T'), ('T1T', 'Y2K'), ('Y2K', 'II0')]:
        print("Test 1: Passed")
    else:
        print("Test 1: Failed")

    
    unordered_circular_list = [('T1T','2QK'),('2QK','UT9'),('1SF','2QK'),('2QK','II0'),('UT9','T1T')]
    ordered_list = solution.find_visit_path(unordered_circular_list)
    if ordered_list == [('1SF','2QK'),('2QK','UT9'),('UT9','T1T'),('T1T','2QK'),('2QK','II0')]:
        print("Test 2: Passed")
    else:
        print("Test 2: Failed")


    many_unordered_lists =  [('T1T','PO9'),('2QK','TX8'),('1SF','2QK'),('Y2K','II0'),('UT9','T1T')]
    ordered_list = solution.find_visit_path(many_unordered_lists)
    if  (
            [('1SF','2QK'),('2QK','TX8')] in ordered_list and\
            [('UT9','T1T'),('T1T','2QK')] in ordered_list and\
            [('Y2K','II0')] in ordered_list 
        ):
        print("Test 3: Passed")
    else:
        print("Test 3: Failed")