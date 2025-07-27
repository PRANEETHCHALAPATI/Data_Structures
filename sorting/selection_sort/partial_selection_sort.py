class Solution:
    def rearrangeArray(self, arr, k):
        # Write your code here...
        n = len(arr)
        for i in range(k):
            min_index = i
            for j in range(i, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
