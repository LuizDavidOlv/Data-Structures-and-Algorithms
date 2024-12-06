nums1 = [1,2,3,0,0]
m = 3
nums2 = [2,5,6,8]
n = 4

def merge(self, nums1, m, nums2, n):
        #* Time Complexity: O((n+m)log(n+m))
        #* Space Complexity: O(1)
        nums1[:] = nums1[:m]
        nums1.extend(nums2)
        nums1.sort()

def merge2(self, nums1, m, nums2, n):
        #* Time Complexity: O(m+n)
        #* Space Complexity: O(1)
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1



merge(merge, nums1, m, nums2, n)
print(nums1)