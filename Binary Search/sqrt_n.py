class solution:
    def findSqrtOfN(self, n):
        #Write your code here...
        low = 0
        high = n
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if mid*mid <= n:
                ans = mid 
                low = mid+1 
            else:
                high = mid-1
        return ans
        
    