class Solution:
    def isSorted(self, arr, n):
        # Write your code here...
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
