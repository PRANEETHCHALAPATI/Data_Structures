class Solution:
    def removeDup(self, arr):
        i = 1
        count = 0
        for j in range(1, len(arr)):
            if arr[j] == arr[j - 1]:
                count += 1
            else:
                count = 0
            if count <= 1:
                arr[i] = arr[j]
                i += 1
        return i
