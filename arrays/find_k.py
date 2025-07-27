class solution:
    def search(self, arr, n, k):
        #Write your code here...
        for i in range(0,n):
            if arr[i] == k:
                return i 
        return -1
    
    