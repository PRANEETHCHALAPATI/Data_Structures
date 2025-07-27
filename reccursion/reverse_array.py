class Solution:
    @staticmethod
    def rev(arr: list, N: int, i: int):
        if i >= N // 2:
            return
        arr[i], arr[N - i - 1] = arr[N - i - 1], arr[i]
        Solution.rev(arr, N, i + 1)

    def reverse(self, arr: list):
        # Start the recursion
        self.rev(arr, len(arr), 0)

# Example usage:
s = Solution()
arr = [1, 2, 3, 4, 5]
s.reverse(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]
