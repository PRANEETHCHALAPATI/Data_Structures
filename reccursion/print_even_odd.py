class Solution:
    @staticmethod
    def print_even(i, n):
        if i == n + 1:
            return
        if i % 2 == 0:
            print(i, end=' ')
        Solution.print_even(i + 1, n)

    @staticmethod
    def print_odd(n):
        if n == 0:
            return
        if n % 2 == 1:
            print(n, end=' ')
        Solution.print_odd(n - 1)

    def print_even_odd(self, n):
        self.print_even(1, n)
        self.print_odd(n)

# Example usage
s = Solution()
s.print_even_odd(10)
