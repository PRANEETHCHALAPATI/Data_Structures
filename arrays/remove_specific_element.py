class Solution:
    def removeSpecificElement(self, arr, target):
        arr[:] = [x for x in arr if x != target]
        return len(arr)
