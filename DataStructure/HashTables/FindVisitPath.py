class Solution:
    # enhance method so it handles ciclic input list
    # unordered_cilic_list = [('T1T','2QK'),('2QK','UT9'),('1SF','2QK'),('2QK','II0'),('UT9','T1T')]
    # enhance method so it handles more than one list as input and output
    # many_unordered_lists =  [('T1T','PO9'),('2QK','TX8'),('1SF','2QK'),('Y2K','II0'),('UT9','T1T')]
    def find_visit_path(self, visitList: list)->list:
        ordered_list = []
        # Step 1: Build a dictionary for quick lookups
        lookup = {first: second for first, second in unordered_list}
        
        # Step 2: Find the start point
        first_elements = set(lookup.keys())
        second_elements = set(lookup.values())
        start_point = first_elements - second_elements

        current = start_point.pop() if start_point else None
        while current in lookup:
            next_point = lookup[current]
            ordered_list.append((current,next_point))
            current = next_point

        return ordered_list


if __name__ == '__main__':
    unordered_list = []# [('T1T','Y2K'),('2QK','UT9'),('1SF','2QK'),('Y2K','II0'),('UT9','T1T')]
    solution = Solution()
    ordered_list = solution.find_visit_path(unordered_list)
    print(ordered_list)
