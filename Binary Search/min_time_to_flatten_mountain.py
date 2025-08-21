class solution:
    def canFind(self,t,h,wt):
        totalTime = 0
        for i in wt:
            left = 0
            right = int(1e6)
            while left <= right:
                mid = left+(right-left)//2 
                tim = (i*((mid)*(mid+1))//2)
                if tim <= t:
                    left = mid+1 
                else:
                    right = mid-1 
            totalTime += right 
            if totalTime >= h:
                return True 
        return totalTime>= h
    def minNumberOfSeconds(self, h, wt):
        #Write your code here...
        start = 0
        end = int(1e18)
        ans = 0
        while(start<=end):
            mid = start+(end-start)//2 
            if self.canFind(mid,h,wt):
                ans = mid 
                end = mid-1 
            else:
                start = mid+1 
        return ans