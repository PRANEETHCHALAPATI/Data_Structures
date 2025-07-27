class Solution:
    def print_divisors(self, n):
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        divisors.sort()
        return divisors

# Example usage
s = Solution()
print(s.print_divisors(36))  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
