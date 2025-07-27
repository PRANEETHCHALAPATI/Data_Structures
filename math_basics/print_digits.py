class Solution:
    def print_digit(self, n):
        while n != 0:
            print(n % 10)
            n = n // 10

# Example usage
s = Solution()
s.print_digit(1234)

