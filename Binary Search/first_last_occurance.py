class solution:
    def firstOccurrence(self, arr, n, k):
        low = 0 
        high = n-1 
        ans = -1 
        while low<=high:
            mid = (low+high)//2 
            if arr[mid] == k:
                ans = mid 
                high = mid-1 
            elif arr[mid]<k:
                low = mid+1 
            else:
                high = mid-1 
        return ans
    
        #Write your code here...

    

    def lastOccurrence(self, arr, n, k):
        #Write your code here...
        low = 0 
        high = n-1 
        ans = -1 
        while low<=high:
            mid = (low+high)//2 
            if arr[mid] == k:
                ans = mid 
                low = mid+1 
            elif arr[mid]<k:
                low = mid+1 
            else:
                high = mid-1 
        return ans
    
    
