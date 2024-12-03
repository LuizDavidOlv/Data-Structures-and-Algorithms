import heapq

class Solution:
    def __init__(self):
        self.min_heap = [] # Store the largest 10% of latencies
        self.max_heap = [] # Store the smallest 90% of latencies( as a max-heap)
        self.count = 0 # Total Number of latencies
      
    # Time complexity of O(logN)
    def AddLatency(self,latency: float):
        self.count += 1
        if not self.max_heap or latency <= -self.max_heap[0]:
            # Insert into max-heap (invert value for max-heap behavior)
            heapq.heappush(self.max_heap, -latency)
        else:
            heapq.heappush(self.min_heap, latency)
        
        # Rebalance the heaps to amintain the 90/10 split
        target_max_heap_size = int(self.count * 0.9)

        # Adjust sizes if necessary
        while  len(self.max_heap) > target_max_heap_size:
            # Move from max_heap to min_heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        while len(self.max_heap) < target_max_heap_size and self.min_heap:
            # Move from min-heap to max-heap
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    

    def getP90(self) -> float:
        # P50 (median) is at the top of the max-heap if heaps are balanced
        if not self.max_heap:
            return None
        
        # The top of the max_heap is the P90 latency
        return -self.max_heap[0]
    
    def ClearData(self):
        self.min_heap.clear()
        self.max_heap.clear()
        self.count = 0
     

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
    result = Lat.getP90()
    print("P90: "+str(result))
    Lat.ClearData()
    print("Data Cleared")
    result = Lat.getP90()
    print("P90: "+str(result))