
# For this problem we will be writing code to record latency information for an API and output the P50 (median) value on demand. We will be writing three functions:
# void AddLatency(int latency) - records a latency measurement in milliseconds
# int GetP50() - returns the P50 (median) latency value based on currently recorded measurements
# void ClearData() - removes all existing latency measurements
# The GetP50() method must execute in constant time. A call to AddLatency() should be as quick as possible given that requirement.

# What data structure is best suited to the task? Please implement the three functions above.
    # The best data structure for this task is balanced binary search tree or a self-balancing binary tree. 
    # Tis structure allows us to efficiently keep track of latencies in sorted order. 
    # Since GetP50() must execute in constant time, we can keep track of the median as a separate variable and update it whenever a new latency is added.
    # A simplet approach is tho use two heaps, one max heap and one min heap. The max heap will store the lower half of the latencies and the min heap will store the upper half.

#? What is the time complexity of adding a latency measurement?
#? How would your implementation change if we wanted a different percentile measurement (for example, P90)?
#? Are there any situations where we could improve the time complexity of adding a latency measurement? For example, what if we know that the API times out after 50ms?
#? How would you test these methods?

import heapq

class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
      
    # Time complexity of O(logN)
    def AddLatency(self,latency: float):
        # Add latency to the appropriate heap
        if not self.max_heap or latency <= self.max_heap[0]:
            heapq.heappush(self.max_heap, -latency)
        else:
            heapq.heappush(self.min_heap, latency)
        
        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    

    def getP50(self) -> float:
        # P50 (median) is at the top of the max-heap if heaps are balanced
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        
        return (-self.max_heap[0] + self.min_heap[0])/2
    
    def ClearData(self):
        self.min_heap.clear()
        self.max_heap.clear()
     

if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    Lat = Solution()
    
    Lat.AddLatency(50)
    Lat.AddLatency(45)
    Lat.AddLatency(2)
    Lat.AddLatency(17099)
    Lat.AddLatency(45)
    Lat.AddLatency(832)
   
    # [50, 45, 46, 1, 2, 17099, 45, 832]
    # [1, 2, 45, 45, 46, 50, 832, 17099]
    result = Lat.getP50()
    print("P50: "+str(result))
    Lat.ClearData()
    print("Data Cleared")
    result = Lat.getP50()
    print("P50: "+str(result))

