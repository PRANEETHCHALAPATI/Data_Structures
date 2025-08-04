import math
class solution:
    def totalTimeToEat(self,arr,m):
        total_time = 0 
        for i in arr:
            total_time += math.ceil(i/m)
        return total_time
    def minimumBananas(self, arr, n, h):
        low = 1
        high = max(arr)
        ans = high 
        while low<=high:
            mid = (low+high)//2 
            
            if self.totalTimeToEat(arr,mid)<=h:
                ans = mid 
                high = mid-1 
            else:
                low = mid+1 
        return ans
        
        
    