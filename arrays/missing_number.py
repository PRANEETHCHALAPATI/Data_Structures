class solution:
    def missingNumber(self, arr, n):
        sum1  = (n*(n+1))//2 
        sum2  = sum(arr)
        return sum1-sum2
       
 
