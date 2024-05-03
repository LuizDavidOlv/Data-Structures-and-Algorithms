import time

class UnoptimizedFibonacci:
    def get_Nth_number(n):
        if n == 1 or n == 2:
            result =  1
        else:
            result = UnoptimizedFibonacci.get_Nth_number(n-1) + UnoptimizedFibonacci.get_Nth_number(n-2)
        return result
    
class MemoizedFibonacci:
    def memoize(n, memo):
        if memo[n] is not None:
            return memo[n]
        if n == 1 or n == 2:
            result = 1
        else:
            result = MemoizedFibonacci.memoize(n-1, memo) + MemoizedFibonacci.memoize(n-2, memo)
        memo[n] = result
        return result

    def get_Nth_number(n):
        memo = [None] * (n+1)
        return MemoizedFibonacci.memoize(n, memo)
    
class BottomUpFibonacci:
    def get_Nth_number(n):
        if n == 1 or n == 2:
            return 1
        bottom_up =  [None] * (n+1)
        bottom_up[1] = 1
        bottom_up[2] = 1
        for i in range(3, n+1):
            bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
        return bottom_up[n]


class main:
    fibonacci_Nth_number = [100]
    for value in fibonacci_Nth_number:
        start_time = time.time()
        result = UnoptimizedFibonacci.get_Nth_number(value)
        stoped_time = time.time()
        elapsedTime = (stoped_time - start_time)
        elapsedTime = elapsedTime if elapsedTime > 0 else 0
        print(f"{value}th is: {result} - Elapsed time: {elapsedTime}")
