class solution:
    def calPainters(self,arr,time):
        count = 1  
        curr_time = 0 
        for i in arr:
            if i+curr_time<=time:
                curr_time += i 
            else:
                count += 1 
                curr_time = i 
        return count
    def paintersPartition(self, arr, k):
        # Write your code here...
        low = max(arr)
        high = sum(arr)
        while low<=high :
            mid = (low+high)//2 
            if self.calPainters(arr,mid) > k:
                low = mid+1 
            else:
                high = mid-1 
        return low