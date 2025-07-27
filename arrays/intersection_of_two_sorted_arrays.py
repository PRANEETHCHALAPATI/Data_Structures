class solution:
    def intersectionSortedArrays(self, a, b):
        #Write your code here...
        ans = [] 
        i=0
        j=0 
        m = len(a)
        n = len(b)
        while i<m and j<n:
            if a[i] == b[j]:
                ans.append(a[i])
                i = i+1 
                j = j+1 
            elif a[i] < b[j]: 
                i = i+1 
            else:
                j = j+1 
        return ans
                
                
    
    