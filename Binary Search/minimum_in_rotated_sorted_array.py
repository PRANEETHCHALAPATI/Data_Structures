class solution:
    def minInArray(self, arr, n):
        #Write your code here...
        ans = float('inf') 
        low = 0 
        high = n-1 
        while low<=high:
            mid = (low+high)//2 
            if arr[low]<=arr[mid]:
                if ans>arr[low]:
                    ans = arr[low] 
                low = mid+1 
            elif arr[mid]<=arr[high]:
                if ans > arr[mid]:
                    ans = arr[mid]
                    high = mid-1 
        return ans
    