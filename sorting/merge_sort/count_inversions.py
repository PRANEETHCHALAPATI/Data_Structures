class Solution:
    @staticmethod
    def merge(arr, left, mid, right):
        i = left
        j = mid + 1
        n = right - left + 1
        inv_count = 0
        temp_arr = [0] * n
        k = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j]
                k += 1
                j += 1
                inv_count += (mid - i + 1)

        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1

        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1

        for c in range(n):
            arr[left + c] = temp_arr[c]

        return inv_count

    @staticmethod
    def merge_sort(arr, left, right):
        if left >= right:
            return 0
        inv_count = 0
        mid = (left + right) // 2
        inv_count += Solution.merge_sort(arr, left, mid)
        inv_count += Solution.merge_sort(arr, mid + 1, right)
        inv_count += Solution.merge(arr, left, mid, right)
        return inv_count

    def countInversions(self, arr):
        return self.merge_sort(arr, 0, len(arr) - 1)
