
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



# namespace Solution
# {
#     public  class Solution {
#         static List<double>  latencyList = new List<double>();
#         public static void Main(string[] args) {

#                // you can write to stdout for debugging purposes, e.g.
#             Console.WriteLine("This is a debug message");
#             AddLatency(50);
#             AddLatency(45);
#             AddLatency(2);
#             AddLatency(17099);
#             AddLatency(45);
#             var result = getP50(latencyList);
#             Console.WriteLine(result);
#         }
#         public static void AddLatency(int num)
#         {
#             latencyList.Add(num);
#             latencyList.Sort();
#         }

#         public static double getP50(List<double> list)
#         {
#             var length = list.Count;
#             int mid = length/2;
#             if((length % 2) == 0)
#             {
#                 var num = list[mid];
#                 return num;
#             }
#             else
#             {
#                 var num =list[mid];
#                 return num;
#             }
#             return 0;
#         }
#     }
# }