class Solution:
    @staticmethod
    def find_fac(n: int) -> int:
        if n == 1 or n == 0:
            return 1
        return n * Solution.find_fac(n - 1)

    def factorial_sequence(self, n: int) -> list[int]:
        result = []
        for i in range(1, n + 1):
            result.append(self.find_fac(i))
        return result

# Example usage
s = Solution()
print(s.factorial_sequence(5))  # Output: [1, 2, 6, 24, 120]
