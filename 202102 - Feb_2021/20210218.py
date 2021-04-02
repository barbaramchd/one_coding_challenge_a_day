"""
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        prime_counts = 0
        if n > 2:
            for number in range(2, n):
                if self.is_prime(number) == True:
                    prime_counts += 1
        else:
            return 0
        return prime_counts + 1

    def is_prime(self, n):
        if n > 1 and n % 2 != 0:
            for number in range(2, n):
                if n % number == 0:
                    return False
            else:
                return True