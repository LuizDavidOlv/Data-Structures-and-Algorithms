from datetime import datetime
from typing import List

class Solution:
    def most_recent_departure(self, departure_times: List[str], current_time: str):
        """
        Returns minutes since the most recent departure strictly before current_time,
        or -1 if none. departure_times is sorted and formatted as 'HH:MM'.
        Time: O(log n), Space: O(1).
        """
        last_departure_obj = None
        current_time_obj = datetime.strptime(current_time, "%H:%M")

        for time in departure_times:
            time_obj = datetime.strptime(time, "%H:%M")
            if time_obj < current_time_obj:
                last_departure_obj = time_obj
            else:
                break

        if last_departure_obj is None:
            return -1
        
        most_recent_departure = int((current_time_obj - last_departure_obj).total_seconds() // 60)
        return most_recent_departure


if __name__ == "__main__":
    departure_times = ["12:30", "14:00", "19:55"]
    current_time = "14:30"
    result = Solution().most_recent_departure(departure_times, current_time)
    print(result)


"""
Imagine you are managing a city's transit archive looking back at past bus departure records. 
You are provided with an array departure_times which lists when buses departed throughout the day. 
Your job is to determine how many minutes have passed since the most recent bus left the station. 
If no bus has departed by the current time, return -1.

Time is formatted as strings in HH:MM within a 24-hour clock. All departures are ordered chronologically.

Assume that a bus scheduled to leave exactly at current_time has not yet departed.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse
than O(departure_times.length × MINUTES_IN_DAY) will fit within the execution time limit.

Example

For departure_times = ["12:30", "14:00", "19:55"] and current_time = "14:30", 
the output should be solution(departure_times, current_time) = 30.

Explanation:
At "14:30", the last bus left at "14:00", so it was 30 minutes ago.

For departure_times = ["00:00", "14:00", "19:55"] and current_time = "00:00", 
the output should be solution(departure_times, current_time) = -1.

Explanation:
No buses have left before "00:00" (the bus scheduled at "00:00" hasn't departed yet), resulting in -1.

For departure_times = ["12:30", "14:00", "19:55"] and current_time = "14:00", 
the output should be solution(departure_times, current_time) = 90.

Explanation:
At "14:00", the last departure was at "12:30" because the "14:00" bus hasn't left, making it 90 minutes ago.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string departure_times

An array of strings detailing bus departures, formatted as HH:MM.

Guaranteed constraints:
3 ≤ departure_times.length ≤ 100.

[input] string current_time

The present time in HH:MM format.

[output] integer

The length of time in minutes since the last bus departed or -1 if none have left before the current time.

"""