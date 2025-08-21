class solution:
    def calDays(self,arr,weight):
        days = 0
        curr_weight = 0
        for i in arr:
            if curr_weight+i <= weight:
               curr_weight += i 
            else:
                curr_weight = i 
                days += 1 
        # print(weight)
        # print(days)
        return days+1
            
    def transportParcels(self, loads, d):
        low = max(loads)
        high = sum(loads)
        ans = high
        while low<=high:
            mid = (low+high)//2 
            if self.calDays(loads,mid) <= d:
                ans = mid 
                high = mid-1
            else:
                low = mid+1 
        return ans