class solution:
    def getSortedSquares(self, arr):
        #Write your code here...
        arr = list(map(lambda x:x*x ,arr))
        
        return sorted(arr)