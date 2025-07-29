class solution:
    def countSubarraysWithBoundedMax(self, arr, minBound, maxBound):
        #Write your code here...
        i = 0 
        j = 0 
        pre_count = 0 
        count = 0 
        while j<len(arr):
            if arr[j]>maxBound:
                pre_count  = 0 
                i = j+1 
            elif minBound<= arr[j] <= maxBound :
                pre_count = j-i+1 
                
            count += pre_count 
            j+= 1 
        return count
                
                