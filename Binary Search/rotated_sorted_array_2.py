class solution:
    def searchRotatedSorted(self, arr, n, k):
        #Write your code here...
        low = 0 
        high = n-1 
        while low<=high:
            mid = (low+high)//2 
            if arr[mid] == k:
                return True 
            elif arr[low] ==  arr[mid] and arr[mid] == arr[high]:
                low += 1 
                high -= 1 
            elif arr[low] <= arr[mid]:
                if arr[low] <= k and k<=arr[mid]:
                    high = mid-1 
                else:
                    low = mid+1 
            elif arr[mid] <= arr[high]:
                if arr[mid] <= k and k<=arr[high]:
                    low = mid+1 
                else:
                    high = mid-1 
        return False
                    
    