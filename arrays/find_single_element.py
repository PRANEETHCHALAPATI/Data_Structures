class solution:
    def findSingleElement(self, arr, n):
        from functools import reduce
        x = reduce(lambda x,y:x^y ,arr)  
        return x
      
            
    
     
