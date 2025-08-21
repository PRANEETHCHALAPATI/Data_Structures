class solution:
    def boquetsFormed(self,arr,i,k):
        y =0 
        count = 0 
        b = 0
        while y < len(arr):
            if arr[y] <= i :
                count += 1 
                if count == k:
                    b+= 1 
                    count=0
            else:
                count = 0 
            y += 1 
        return b
                
                
    def bouquetFormation(self, arr, n, k, m):
        low = min(arr)
        high = max(arr)
        ans = -1
        if m*k > n :
            return ans
        while low <= high:
            mid = (low+high)//2 
            
            if self.boquetsFormed(arr,mid,k) >= m:
                ans = mid 
                high = mid-1 
            else:
                low = mid+1 
        return ans
        
    