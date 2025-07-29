class solution:
    def findMissingAndRepeating(self, arr, n):
        #Write your code here...
        set_x = set(arr) 
        
        xor1 = 0 
        xor2 = 0 
        xor3 = 0
        for i in set_x:
            xor1 ^= i 
        for i in arr:
            xor2 ^= i 
        for i in range(1,n+1):
            xor3 ^= i
        dup = xor1^xor2 
        miss = xor1^xor3 
        return [dup,miss]
        