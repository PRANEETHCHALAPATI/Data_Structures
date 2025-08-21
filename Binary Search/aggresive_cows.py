class solution:
    def isPossible(self,arr,distance,c):
        count = 1
        last = arr[0]
        n = len(arr)
        for i in range(1,n):
            if arr[i]-last >= distance :
                count += 1 
                last = arr[i]
            if count >= c:
                return True 
        return False
    def aggressiveCows(self, arr, c):
        #Write your code here.... 
        arr.sort() 
        low = 1 
        n = len(arr)
        high = arr[n-1]-arr[0]
        while low<=high:
            mid = (low+high)//2 
            if self.isPossible(arr,mid,c): 
                low = mid+1 
            else:
                high = mid-1 
        return high
                
        
