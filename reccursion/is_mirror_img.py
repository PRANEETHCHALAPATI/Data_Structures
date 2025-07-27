class Solution:
    def check(self, arr, i, n):
        if i >= n:
            return True
        if arr[i] != arr[n]:
            return False
        return self.check(arr, i + 1, n - 1)

    def isMirrorImage(self, arr):
        return self.check(arr, 0, len(arr) - 1)

# Example usage:
sol = Solution()
arr = [1, 2, 3, 2, 1]
print(sol.isMirrorImage(arr))  # Output: True

arr2 = [1, 2, 3, 4, 5]
print(sol.isMirrorImage(arr2))  # Output: False
