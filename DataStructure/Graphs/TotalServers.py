'''
Developers at Dell have deployed an application with a distributed database. It is stored on total_servers different servers numbered from 1 to total_servers that are connected in a circular fashion, i.e., 1 is connected to 2, 2 is connected to 3, and so on until total_servers connects back to 1.

There is a subset of servers represented by an array servers of n integers. They need to transfer the data to each other to be synchronized. Data transfer from one server to one it is directly connected to takes 1 unit of time. Starting from any server, find the minimum amount of time to transfer the data to all the other servers.

Example:

Suppose total_servers = 8, n = 3, servers = [2, 6, 8].

Two possible paths are shown, but there can be many more. One path goes from 2 to 6 to 8, taking 6 units of time. The other path goes from 2 to 8 to 6 and takes 4 units of time. Return the shorter path length, which is 4.

Function Description
Complete the function getMinTime in the editor below.

getMinTime takes the following arguments:
int total_servers: The number of servers in the system
int servers[n]: The servers to share the data with

Returns:
int: The minimum time required to transfer the data on all the servers

Constraints:
1 <= total_servers <=  10^9
1 <= n <= 10 
1 <= servers[i] <= n
'''

class Solution:
    def getMinTime(self, total_servers, servers):
        n = len(servers)
        servers.sort()
        
        max_gap = 0
        for i in range(n):
            current_server = servers[i]

            #? The modulo operation (%) calculates the remainder when one number is divided by another.
            #?  It is particularly useful for handling cyclic or circular patterns.
            next_server = servers[(i + 1) % n]

            # Calculate the gap between the current and next server in a circular fashion
            # Adding total_servers ensures positive results when wrapping around
            gap = (next_server - current_server + total_servers) % total_servers

            # If the gap is 0 (e.g., two servers occupy the same spot in the circular arrangement),
            # consider the gap as the total number of servers
            if gap == 0:
                gap = total_servers

            max_gap = max(max_gap, gap)
        
        if max_gap == total_servers or max_gap == 0:
            return 0
        else:
            return total_servers - max_gap


if __name__ == '__main__':
    solution = Solution()
    total_servers= 8
    servers= [2,4,8]
    result = solution.getMinTime(total_servers,servers)
    if result == 4:
        print('pass')
    else:
        print(f'servers {servers} failed')
    

    # Test case 2
    total_servers = 8
    servers = [2, 6, 8]
    result = solution.getMinTime(total_servers, servers)
    if result == 4:
        print('pass')
    else:
        print(f'servers {servers} failed')

    # Test case 3
    total_servers = 12
    servers = [3, 9, 12]
    result = solution.getMinTime(total_servers, servers)
    if result == 6:
        print('pass')
    else:
        print(f'servers {servers} failed')

    # Test case 4
    total_servers = 10
    servers = [1, 5, 9]
    result = solution.getMinTime(total_servers, servers)
    if result == 6:
        print('pass')
    else:
        print(f'servers {servers} failed')

    # Test case 5
    total_servers = 15
    servers = [2, 8, 14]
    result = solution.getMinTime(total_servers, servers)
    if result == 9:
        print('pass')
    else:
        print(f'servers {servers} failed')

    # Test case 6
    total_servers = 20
    servers = [4, 10, 16]
    result = solution.getMinTime(total_servers, servers)
    if result == 12:
        print('pass')
    else:
        print(f'servers {servers} failed')

    # Test case 7
    total_servers = 9
    servers = [3, 6, 9]
    result = solution.getMinTime(total_servers, servers)
    if result == 6:
        print('pass')
    else:
        print(f'servers {servers} failed')

    # Test case 8
    total_servers = 5
    servers = [1, 3, 5]
    result = solution.getMinTime(total_servers, servers)
    if result == 3:
        print('pass')
    else:
        print(f'servers {servers} failed')

    # Test case 9
    total_servers = 7
    servers = [2, 5, 7]
    result = solution.getMinTime(total_servers, servers)
    if result == 4:
        print('pass')
    else:
        print(f'servers {servers} failed')

    # Test case 10
    total_servers = 11
    servers = [1, 6, 11]
    result = solution.getMinTime(total_servers, servers)
    if result == 6:
        print('pass')
    else:
        print(f'servers {servers} failed')


