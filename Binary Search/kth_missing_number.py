class solution:
    def kthMissingNumber(self, arr, k):
        #Write your code here...    
        low = 0 
        high = len(arr)-1  
        while low<=high:
            mid = (low+high)//2
            if arr[mid]-mid-1<k:
                low = mid+1 
            else:
                high = mid-1 
        return low+k 
     
        