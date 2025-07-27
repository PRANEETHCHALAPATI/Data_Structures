class Solution:
    def print_1_to_n_in_ascending_order(self, N):
        if N == 0:
            return
        self.print_1_to_n_in_ascending_order(N - 1)
        print(N)

# Example usage
s = Solution()
s.print_1_to_n_in_ascending_order(5)
