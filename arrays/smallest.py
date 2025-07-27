class Solution:
    def smallestElement(self, arr, n):
        min_val = arr[0]
        for i in range(1, n):
            if arr[i] < min_val:
                min_val = arr[i]
        return min_val
