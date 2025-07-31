class solution:
    def numberOfOccurences(self, arr, n, k):
        #Write your code here...
        first = -1 
        last = -1 
        
        low = 0 
        high = n-1 
        while low<=high:
            mid = (low+high)//2 
            if arr[mid] == k:
                first = mid 
                high = mid-1 
            elif arr[mid]<k:
                low = mid+1 
            else:
                high = mid-1 
        
        low = 0 
        high = n-1 
        while low<=high:
            mid=(low+high)//2 
            if arr[mid]==k:
                last = mid 
                low = mid+1 
            elif arr[mid]<k:
                low = mid+1 
            else:
                high = mid-1 
        
        if first ==  -1:
            return 0 
        else:
            return last-first+1
                
    
