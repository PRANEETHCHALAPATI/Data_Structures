class solution:
    def searchRotatedSorted(self, arr, n, x):
        #Write your code here...
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]==x:
                return mid
            if arr[low]<=arr[mid]:
                if arr[low]<=x and x<=arr[mid]:
                    high = mid-1 
                else:
                    low=mid+1 
            elif arr[mid]<=arr[high]:
                if arr[mid]<=x and x<=arr[high]:
                    low=mid+1 
                else:
                    high = mid-1 
        return -1
                