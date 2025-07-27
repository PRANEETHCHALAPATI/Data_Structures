class Solution:
    @staticmethod
    def isPrime(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        return count == 2

    def sumOfPrimeFibonacci(self, n):
        sum_ = 0
        v = [0, 1]
        for i in range(2, n + 1):
            v.append(v[i - 2] + v[i - 1])
        for i in v:
            if self.isPrime(i):
                sum_ += i
        return sum