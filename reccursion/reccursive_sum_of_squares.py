class Solution:
    def recursive_sum_of_squares(self, n: int) -> int:
        if n == 1:
            return 1
        return self.recursive_sum_of_squares(n - 1) + n * n

# Example usage
s = Solution()
print(s.recursive_sum_of_squares(3))  # Output: 14 (1² + 2² + 3²)
