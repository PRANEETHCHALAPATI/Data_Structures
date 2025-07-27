class solution:
    def unionOfTwoSortedArrays(self, a, b):
        #Write your code here...
        set_a = set(a)
        set_b = set(b)
        set_res = set_a.union(set_b)
        arr = list(set_res)
        
        return sorted(arr)
    
        