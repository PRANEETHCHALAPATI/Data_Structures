class solution:
    def evenly_divides(self, N):
        #Write your code here...
        string = str(N)
        count = 0
        for i in string:
            if N%int(i) == 0:
                count += 1 
        return count