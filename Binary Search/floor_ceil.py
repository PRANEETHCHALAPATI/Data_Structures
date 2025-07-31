class solution:
    def arrayCeil(self, arr, n, k):
        #Write your code here...
        low = 0 
        high = n-1 
        ans = -1 
        while low<=high:
            mid = (low+high)//2 
            if arr[mid]>= k:
                ans = arr[mid]
                high = mid-1 
            else:
                low = mid+1 
        return ans
        
    
    def arrayFloor(self, arr, n, k):
        #Write your code here...
        low = 0 
        high = n-1 
        ans = -1 
        while low<=high:
            mid = (low+high)//2 
            if arr[mid]<=k:
                ans = arr[mid]
                low = mid+1 
            else:
                high = mid-1 
        return ans