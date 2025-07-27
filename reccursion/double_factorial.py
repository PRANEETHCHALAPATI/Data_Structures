class Solution:
    def double_factorial(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return n * self.double_factorial(n - 2)

# Example usage
s = Solution()
print(s.double_factorial(7))  # Output: 105 (7 × 5 × 3 × 1)
