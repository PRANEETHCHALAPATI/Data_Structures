class Solution:
    def reverseArraySection(self, arr, left, right):
        if left >= right:
            return
        arr[left], arr[right] = arr[right], arr[left]
        self.reverseArraySection(arr, left + 1, right - 1)

# Example usage:
sol = Solution()
arr = [1, 2, 3, 4, 5]
sol.reverseArraySection(arr, 1, 3)
print(arr)  # Output: [1, 4, 3, 2, 5]
