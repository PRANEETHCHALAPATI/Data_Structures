class solution:
    def calStudents(self,arr,pages):
        count = 1
        curr_pages = 0 
        for i in arr:
            if curr_pages+i<=pages:
                curr_pages += i 
            else:
                count +=1 
                curr_pages = i 
        return count
    def bookAllocation(self, arr, k):
        # Write your code here...
        low = max(arr)
        high = sum(arr)
        while low<=high:
            mid = (low+high)//2 
            if self.calStudents(arr,mid)>k:
                low = mid+1  
            else:
                high = mid-1 
        return low
                