class solution:
    def medianSortedArrays(self, arr1, arr2):
        # Write your code here...
        arr1.extend(arr2) 
        arr1.sort()
        n = len(arr1)
        if n%2 == 1:
            mid = n//2 
            return arr1[mid] 
        else:
            mid1 = n//2 
            mid2 = mid1-1 
            return (arr1[mid1]+arr1[mid2])/2
            