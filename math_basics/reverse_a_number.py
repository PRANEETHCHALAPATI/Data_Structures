class solution:
    def reverseNumber(self, N):
        #Write your code here...
        num = 0
        while(N!=0):
            temp = N%10 
            N  = int(N/10) 
            num  = num*10 + temp
        return num
            