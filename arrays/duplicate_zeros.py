class solution:
    def duplicateZeros(self, arr):
        #Write your code here...
        n = len(arr)
        i = 0
        while i < n :
            if arr[i] == 0:
                arr.insert(i+1,0)
                i += 2 
            else:
                i+=1 
        n1 = len(arr)
        for i in range(n1-n):
            arr.pop()