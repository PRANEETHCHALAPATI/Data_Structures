class Solution:
    def selectionSort(self, arr, n):
        # Write your code here...
        for i in range(n - 1):
            min_index = i
            for j in range(i, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
