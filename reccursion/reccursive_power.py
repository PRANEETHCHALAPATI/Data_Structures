class Solution:
    def recursive_power(self, a: float, b: int) -> float:
        if b == 1:
            return a
        return a * self.recursive_power(a, b - 1)

# Example usage
s = Solution()
print(s.recursive_power(2, 3))  # Output: 8.0
