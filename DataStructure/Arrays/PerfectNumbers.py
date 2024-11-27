from typing import List


class Solution:
    def getPerfectNumbersList(self, num: int):
        primes = self.get_prime_numbers(num)

        #? Sets are implemented using hashing, which makes operations like adding, removing, and checking extremely effient 
        prime_set = set(primes)
        
        output = []

        for prime in primes:
            complement = num - prime
            if complement in prime_set and complement >= prime:
                output.append([prime, complement])

        return output

    
    def get_prime_numbers(self, num: int) -> List[int]:
        return self.sieve_of_erathosthene(num)
    
    def sieve_of_erathosthene(self, n: int):
        # Best for generating all primes up to a large number n.
        # Simple, fast and commonly used in applications
        is_prime = [True]*(n+1)
        is_prime[0] = is_prime[1] = False

        test = []

        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    test.append(j)
                    is_prime[j] = False

        return [i for i in range(n+1) if is_prime[i]]


if __name__ == '__main__':
    num = 18
    result = Solution().getPerfectNumbersList(num)