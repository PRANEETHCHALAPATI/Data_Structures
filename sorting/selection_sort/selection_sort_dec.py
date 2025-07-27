class Solution:
    def selectionSort(self, arr, n):
        # Write your code here...
        for i in range(n - 1):
            max_index = i
            for j in range(i, n):
                if arr[max_index] < arr[j]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]
