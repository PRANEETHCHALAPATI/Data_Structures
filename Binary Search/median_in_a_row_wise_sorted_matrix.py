import bisect
class solution:
   
    def findMedian(self,grid, r, c):
        #Write your code here...
        minVal = float('inf')
        maxVal = float('-inf')
        for i in range(r):
            if minVal>grid[i][0]:
                minVal = grid[i][0]
            if maxVal<grid[i][-1]:
                maxVal = grid[i][-1] 
        pos = (r*c+1)//2
        while minVal<=maxVal:
            midVal = (minVal+maxVal)//2 
            count = 0  
            for i in range(r):
                count += bisect.bisect_right(grid[i],midVal) 
            if count<pos:
                minVal = midVal+1  
            else:
                maxVal = midVal-1 
        return minVal
            