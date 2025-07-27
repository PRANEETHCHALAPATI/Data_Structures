class Solution:
    def countSwaps(self, arr):
        n = len(arr)
        count = 0
        for i in range(1, n):
            j = i
            while j >= 1 and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                count += 1
                j -= 1
        return count
