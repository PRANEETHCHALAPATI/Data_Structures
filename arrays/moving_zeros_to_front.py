class Solution:
    def moveZerosToFront(self, arr, n):
        i = n - 1
        for j in range(n - 1, -1, -1):
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                i -= 1
