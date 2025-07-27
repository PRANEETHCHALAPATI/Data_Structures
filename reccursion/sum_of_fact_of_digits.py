class Solution:
    @staticmethod
    def find_fac(n: int) -> int:
        if n == 1 or n == 0:
            return 1
        return n * Solution.find_fac(n - 1)

    def sum_of_factorials_of_digits(self, n: int) -> int:
        if n == 0:
            return 0
        return self.find_fac(n % 10) + self.sum_of_factorials_of_digits(n // 10)

# Example usage
s = Solution()
print(s.sum_of_factorials_of_digits(145))  # Output: 145 (1! + 4! + 5!)
