class Solution:
    def print_1_to_n_in_descending_order(self, N):
        if N == 0:
            return
        print(N)
        self.print_1_to_n_in_descending_order(N - 1)

# Example usage
s = Solution()
s.print_1_to_n_in_descending_order(5)
