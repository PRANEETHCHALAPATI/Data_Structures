class Solution:
    def removeDuplicates(self, arr, n):
        # Write your code here...
        i = 0
        for j in range(1, n):
            if arr[i] != arr[j]:
                arr[i + 1] = arr[j]
                i += 1
        return i + 1

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 5]
    n = len(arr)
    solution = Solution()
    new_length = solution.removeDuplicates(arr, n)
    print("Array after removing duplicates:", arr[:new_length])
    print("New length of the array:", new_length)