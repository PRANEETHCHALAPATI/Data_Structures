class Solution:
    def recursion_sum(self, N: int) -> int:
        if N == 1:
            return 1
        return N + self.recursion_sum(N - 1)

# Example usage
s = Solution()
print(s.recursion_sum(5))  # Output: 15 (1 + 2 + 3 + 4 + 5)
