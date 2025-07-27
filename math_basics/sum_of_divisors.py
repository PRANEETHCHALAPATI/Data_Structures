class Solution:
    def sum_of_divisors(self, num):
        total = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        return total

# Example usage
s = Solution()
print(s.sum_of_divisors(12))  # Output: 28 (1 + 2 + 3 + 4 + 6 + 12)
