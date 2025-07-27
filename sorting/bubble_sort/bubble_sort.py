class Solution:
    def bubbleSort(self, arr):
        # Write your code here...
        n = len(arr)
        for i in range(n - 1, 0, -1):
            sorted_flag = True
            for j in range(i):
                if arr[j + 1] < arr[j]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    sorted_flag = False
            if sorted_flag:
                break
