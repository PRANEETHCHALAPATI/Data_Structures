class Solution:
    def secondLargestElement(self, arr, n):
        max_val = arr[0]
        second_max = -1
        for i in range(n):
            if arr[i] > max_val:
                second_max = max_val
                max_val = arr[i]
            if arr[i] > second_max and arr[i] < max_val:
                second_max = arr[i]
        return second_max
