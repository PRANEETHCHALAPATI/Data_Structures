class Solution:
    @staticmethod
    def partition(arr, low, high):
        i = low
        j = high
        while i < j:
            while i < high and arr[low] >= arr[i]:
                i += 1
            while j > 0 and arr[j] > arr[low]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

    @staticmethod
    def quick_sort(arr, low, high):
        if low < high:
            j = Solution.partition(arr, low, high)
            Solution.quick_sort(arr, low, j - 1)
            Solution.quick_sort(arr, j + 1, high)

    def quickSort(self, arr, n):
        self.quick_sort(arr, 0, n - 1)
