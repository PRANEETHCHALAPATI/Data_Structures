import math
class solution:
    def cal_sum(self,arr,divisor):
        total_sum = 0 
        for i in arr:
            total_sum += math.ceil(i/divisor)
        return total_sum
    def minimumPositiveDivisor(self, arr, n, limit):
        #Write your code here...
        low = 1 
        high = max(arr) 
        ans = high
        while low<=high:
            mid = (low+high)//2 
            
            if self.cal_sum(arr,mid) <= limit:
                ans = mid 
                high = mid-1 
            else:
                low = mid+1 
        return ans
    