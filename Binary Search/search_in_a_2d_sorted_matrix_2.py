class solution:
    def searchGridII(self, grid, target):
        #Write your code here...
        n = len(grid)
        m = len(grid[0])
        row = 0 
        col = m-1 
        while row<n and col >=0:
            if grid[row][col] == target:
                return True 
            elif grid[row][col] > target:
                col -= 1 
            else:
                row += 1
        return False