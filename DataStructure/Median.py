
# For this problem we will be writing code to record latency information for an API and output the P50 (median) value on demand. We will be writing three functions:

# void AddLatency(int latency) - records a latency measurement in milliseconds

# int GetP50() - returns the P50 (median) latency value based on currently recorded measurements

# void ClearData() - removes all existing latency measurements

# The GetP50() method must execute in constant time. A call to AddLatency() should be as quick as possible given that requirement.


# What data structure is best suited to the task? Please implement the three functions above.

# What is the time complexity of adding a latency measurement?

# How would your implementation change if we wanted a different percentile measurement (for example, P90)?

# Are there any situations where we could improve the time complexity of adding a latency measurement? For example, what if we know that the API times out after 50ms?

# How would you test these methods?

import bisect
class Latency:
        def __init__(self):
             self.latencyList: list[float] = []
      
        def AddLatency(self,num: float):
            # self.latencyList.append(num)
            # self.latencyList.sort()
            bisect.insort(self.latencyList, num)
        

        def getP50(self) -> float:
            if(len(self.latencyList) == 0):
                return 0
            list = self.latencyList
            length = len(list)
            mid: int = length//2
            if((length % 2) == 0):
                num1 = list[mid]
                num2 = list[mid-1]
                num = (num1+num2)/2
                return num
            else:
                num =list[mid]
                return num
        
        def ClearData(self):
            self.latencyList.clear()

if __name__ == '__main__':
    clear_terminal = "\033[H\033[J"
    print(clear_terminal)
    Lat = Latency()
    Lat.AddLatency(50)
    Lat.AddLatency(45)
    Lat.AddLatency(2)
    Lat.AddLatency(17099)
    Lat.AddLatency(45)
    Lat.AddLatency(832)
    result = Lat.getP50()
    print("P50: "+str(result))
    Lat.ClearData()
    print("Data Cleared")
    result = Lat.getP50()
    print("P50: "+str(result))

