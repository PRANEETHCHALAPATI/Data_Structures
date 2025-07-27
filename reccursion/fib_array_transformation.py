class Solution:
    @staticmethod
    def getFib(n):
        if n == 0 or n == 1:
            return n
        return Solution.getFib(n - 1) + Solution.getFib(n - 2)

    def getTransformedArray(self, arr, n):
        # Code Here
        v = []
        for i in range(n):
            v.append(self.getFib(arr[i]))
        return v
