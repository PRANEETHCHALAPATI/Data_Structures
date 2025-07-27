class Solution:
    def minSwaps(self, arr):
        count = 0
        temp_array = arr.copy()
        temp_array.sort()
        index_map = {val: idx for idx, val in enumerate(temp_array)}

        i = 0
        while i < len(arr):
            if index_map[arr[i]] == i:
                i += 1
            else:
                swap_idx = index_map[arr[i]]
                arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
                count += 1
        return count
