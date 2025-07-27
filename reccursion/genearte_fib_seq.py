class Solution:
    def generateGeneralizedFibonacci(self, k, start, n):
        # Code Here
        if n - k == 0:
            return start
        temp = 0
        for i in range(len(start) - k, len(start)):
            temp += start[i]
        start.append(temp)
        return self.generateGeneralizedFibonacci(k, start, n - 1)
