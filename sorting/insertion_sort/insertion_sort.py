class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            j = i
            while j >= 1 and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
