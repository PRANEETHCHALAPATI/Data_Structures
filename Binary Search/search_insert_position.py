class solution:
    def searchInsertPosition(self, arr, n, k):
        #Write your code here...
        i  =  0 
        j = n-1 
        ans = n
        while i<=j:
            mid = (i+j)//2 
            if arr[mid] >= k:
                ans = mid 
                j = mid-1 
            else:
                i = mid+1
        return ans
            
    
    