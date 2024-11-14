
# Dell provides fast and efficent server solutions. The developers want to stress=test the quality of the servers' channels. They must ensure the following:
    # 1-Each of the packets must be sent via a single channel
    # 2-Each of the channels must transfer at least one packet
#The quality of the transfer for a channel is defined by the median of the sizes of all the data packets sent through that channel.
#Note: The median of an array is the value in the middle of the array when it is sorted in ascending order. If the array has an even number of elements, the median is the average of the two middle elements.
#Find the max possible sum of the qualities of all channels. If the answer is a floating-point value, round it to the nest higher integer.

import math
from statistics import median


class Solution:
    def distribute_packets(self, channels, packets):
        channels_queue = [[] for _ in range(channels)]

        # Distribute the largest packets to the first channels
        for i in range(channels - 1):
            channels_queue[i].append(packets.pop(0))

        # Add remaining packets to the last channel
        channels_queue[-1].extend(packets)

        return channels_queue

    def find_max_quality(self, packets, channels):
        packets.sort(reverse=True)
        n = len(packets)
        if channels >= n:
            return sum(packets)
        
        channels_queue = self.distribute_packets(channels, packets)
        channels_quality = [median(queue) for queue in channels_queue]
        
        # Use math.ceil for rounding up if necessary
        max_quality = math.ceil(sum(channels_quality))
        return max_quality

if __name__ == '__main__':
    packets = [2,2,1,5,3]
    channels = 3
    solution = Solution()
    result = solution.find_max_quality(packets, channels)
    #result should be 7
    print('The max possible sum of the qualities of all channels is: ', result)