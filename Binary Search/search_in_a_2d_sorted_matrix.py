class solution:
    def searchArr(self,arr,target):
        n = len(arr)
        low = 0 
        high = n-1 
        while low<=high:
            mid = (low+high)//2 
            if arr[mid] == target:
                return True 
            elif arr[mid]>target:
                high = mid-1 
            else:
                low = mid+1 
        return False
    def searchGrid(self, grid, target):
        n = len(grid)
        low = 0 
        high = n-1 
        while low<=high:
            mid = (low+high)//2 
            temp = self.searchArr(grid[mid],target)
            if temp:
                return True 
            else:
                if grid[mid][0] > target:
                    high = mid-1 
                else:
                    low = mid+1 
        return False
        