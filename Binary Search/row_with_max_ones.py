class solution:
    def findOnes(self,arr):
        low = 0 
        high = len(arr)-1 
        ans = high 
        while low<=high:
            mid = (low+high)//2 
            if arr[mid] == 1:
                ans = mid 
                high = mid-1
            else:
                low = mid+1 
        return len(arr)-ans
    def rowWithMaxOnes(self, matrix):
        #Write your code here...
        max_ones = 0 
        index = 0
        for i in range(len(matrix)):
            x = self.findOnes(matrix[i])
            if x>max_ones:
                max_ones = x 
                index = i
        if index == 0:
            return -1
        else:
            return index
        
        