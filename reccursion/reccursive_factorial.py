class Solution:
    def recursion_factorial(self, n: int) -> int:
        if n == 1:
            return 1
        return n * self.recursion_factorial(n - 1)

# Example usage
s = Solution()
print(s.recursion_factorial(5))  # Output: 120
