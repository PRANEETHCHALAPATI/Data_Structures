class solution:
    def findPow(self,i,n):
        res = 1 
        for j in range(n):
            res *= i 
        return res
    def findNthrootofM(self, n, m):
        low =  1 
        high = m 
        while low<=high:
            mid = (low+high)//2 
            if self.findPow(mid,n) == m:
                return mid 
            elif self.findPow(mid,n) < m:
                low = mid+1 
            else:
                high = mid-1 
        return -1
         
    