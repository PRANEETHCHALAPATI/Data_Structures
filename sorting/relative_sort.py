class Solution:
    def relativeSort(self, arr1, arr2):
        final_array = []

        for i in arr2:
            for j in range(len(arr1)):
                if i == arr1[j]:
                    final_array.append(arr1[j])
                    arr1[j] = -1  # Mark as used

        arr1.sort()
        for i in arr1:
            if i != -1:
                final_array.append(i)

        return final_array
