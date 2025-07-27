class Solution:
    def fibNum(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fibNum(N - 1) + self.fibNum(N - 2)
