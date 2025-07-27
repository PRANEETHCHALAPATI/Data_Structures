class Solution:
    def secondSmallestElement(self, arr, n):
        min_val = arr[1]
        second_min = 1001
        for i in range(n):
            if arr[i] < min_val:
                second_min = min_val
                min_val = arr[i]
            if arr[i] < second_min and arr[i] > min_val:
                second_min = arr[i]
        return second_min
