class solution:
    def leftRotate(self, arr, n, k):
        #Write your code here...
        k = k%n 
        arr[:k] = reversed(arr[:k])
        arr[k:] = reversed(arr[k:])
        arr[:] = reversed(arr[:])  
    
    