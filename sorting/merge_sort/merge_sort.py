class Solution:
    @staticmethod
    def merge(arr, left, mid, right):
        i = left
        j = mid + 1
        k = 0
        n = right - left + 1
        new_array = [0] * n

        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                new_array[k] = arr[i]
                k += 1
                i += 1
            else:
                new_array[k] = arr[j]
                k += 1
                j += 1

        while i <= mid:
            new_array[k] = arr[i]
            k += 1
            i += 1

        while j <= right:
            new_array[k] = arr[j]
            k += 1
            j += 1

        for c in range(n):
            arr[left + c] = new_array[c]

    @staticmethod
    def merge_sort(arr, left, right):
        if left == right:
            return
        mid = (left + right) // 2
        Solution.merge_sort(arr, left, mid)
        Solution.merge_sort(arr, mid + 1, right)
        Solution.merge(arr, left, mid, right)

    def mergeSort(self, arr):
        self.merge_sort(arr, 0, len(arr) - 1)
