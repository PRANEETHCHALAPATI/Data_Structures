class solution:
    def findMaxRowIndex(self,grid,n,col):
        max_val = -1
        max_index = -1
        for i in range(n):
            if grid[i][col] > max_val:
                max_val = grid[i][col]
                max_index = i 
        return max_index
    def findPeakElement(self, grid):
        #Write your code here...
        n = len(grid)
        m = len(grid[0]) 
        low = 0 
        high = m-1 
        while low<=high:
            mid = (low+high)//2 
            max_row_index = self.findMaxRowIndex(grid,n,mid)
            if mid-1>=0:
                left = grid[max_row_index][mid-1]
            else:
                left = -1 
            if mid+1<m:
                right = grid[max_row_index][mid+1]
            else:
                right = -1 
            x = grid[max_row_index][mid] 
            if x>left and x>right:
                return [max_row_index,mid]
            elif x>left :
                low = mid+1 
            else:
                high = mid-1
        return[-1,-1]