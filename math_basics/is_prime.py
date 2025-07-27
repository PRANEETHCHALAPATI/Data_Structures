class Solution:
    def is_prime(self, n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        return count == 2

# Example usage
s = Solution()
print(s.is_prime(7))   # True
print(s.is_prime(9))   # False
