class solution:
    def maxConsecutiveOnes(self, arr, n):
        #Write your code here...
        curr = 0 
        max_ones = 0 
        for i in arr:
            if i == 1:
                curr += 1 
                if (curr > max_ones):
                    max_ones = curr  
            else:
                curr = 0 
        return max_ones
                    
    
     
