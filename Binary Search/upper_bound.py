class solution:
    def upperBound(self, arr, n, x):
        # Write your code here...
        ans = n 
        i = 0 
        j = n-1 
        while i<=j:
            mid = (i+j)//2 
            if arr[mid]>x:
                ans = mid 
                j = mid-1 
            else:
                i = mid+1  
        return ans
